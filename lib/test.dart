import 'dart:math';



main (List<String> args) {
  String data = "POST&%2F&Timestamp%3D2022-09-19T08%253A59%253A34Z%26Uuid%3D46e2a8ef-f0c4-4a8f-b018-4982baa7e84d%26id%3D129%26idCard%3D123456789012345678%26personName%3D1%26phone%3D12345678901%26randstr%3D%2540h2y%26ticket%3Dt039Ob0vfqiuwqCv99PjVdyFxwmmdo-hNwcAficki8A-sZxk-bf5BkB2cWzYnTyWEM72EC2-Qycgic8r6qRtguO_iX3_zz-RPalgMTM80VjYHJlIvS6XD_-XFnB6pWbU4uwvPUJHMilOmQ%252A";
  KaiwuSignature sign = KaiwuSignature(params: {});
  print(data);
}

import 'dart:convert';

import 'package:crypto/crypto.dart';
import 'package:date_format/date_format.dart';
import 'package:uuid/uuid.dart';
import 'package:kaiwu_app/service/config.dart';
import 'package:kaiwu_app/service/http_request.dart';

class KaiwuSignature {
  Map<String, dynamic> params;
  String time = getFormatTime();
  String uuid = getUUID();

  KaiwuSignature({required this.params}) {
    params["Timestamp"] = time;
    params["Uuid"] = uuid;
  }


  static String replaceSpecialEncode (String value) {
    return Uri.encodeComponent(value)
      .replaceAll("+", "%20")
      .replaceAll("*", "%2A")
      .replaceAll("%7E", "~");
  }

  static Map<String, dynamic> sortParamKeys (Map<String, dynamic> params) {
    List<String> keys = params.keys.toList();
    keys.sort((a, b) {
      List<int> aLetters = a.codeUnits;
      List<int> bLetters = b.codeUnits;
      for (int index = 0; index < aLetters.length; index++) {
        if (bLetters.length <= index) return 1;
        if (aLetters[index] > bLetters[index]) {
          return 1;
        } else if (aLetters[index] < bLetters[index]) {
          return -1;
        }
      }
      return 0;
    });
    Map<String, dynamic> treeMap = {};
    for (String element in keys) {
      treeMap[element] = params[element];
    }
    return treeMap;
  }

  static String generateSortedSignature (Map<String, dynamic> treeMap) {
    String generatedData = "";
    treeMap.forEach((key, value) {
      generatedData += "&";
      generatedData += replaceSpecialEncode(key);
      generatedData += "=";
      generatedData += replaceSpecialEncode(value);
    });
    return generatedData;
  }

  static String concatSignatureString (HTTP method, String generatedData) {
    String signatureData = "";
    signatureData += method2String(method);
    signatureData += "&";
    signatureData += replaceSpecialEncode("/");
    signatureData += "&";
    signatureData += replaceSpecialEncode(generatedData);
    print(signatureData);
    return signatureData;
  }

  static String sign (String signatureData) {
    List<int> key = utf8.encode(SignatureConfig.accessSecret);
    List<int> data = utf8.encode(signatureData);
    Hmac mac = Hmac(sha1, key);
    Digest digest = mac.convert(data);
    print(base64Encode(digest.bytes));
    print("base64Encode: " + const Base64Encoder().convert(digest.bytes));
    return replaceSpecialEncode(const Base64Encoder().convert(digest.bytes));
  }

  //java.util.TreeMap<String, String> sortParas = new java.util.TreeMap<>(paras);

  // public static String sign(String accessSecret, String stringToSign) throws Exception {
  //   javax.crypto.Mac mac = javax.crypto.Mac.getInstance("HmacSHA1");
  //   mac.init(new javax.crypto.spec.SecretKeySpec(accessSecret.getBytes("UTF-8"), "HmacSHA1"));
  //   byte[] signData = mac.doFinal(stringToSign.getBytes("UTF-8"));
  //   return new sun.misc.BASE64Encoder().encode(signData);
  // }


  static String getUUID () {
    // ignore: prefer_const_constructors
    return Uuid().v4();
  }

  static String getFormatTime() {
    DateTime now = DateTime.now();
    String formatTime = formatDate(
      now,
      [yyyy, '-', mm, '-', dd, 'T', HH, ':', nn, ':', ss]
    );
    print(formatTime);
    return formatTime+"Z";
  }

  String signature (HTTP method) {
    Map<String, dynamic> treeMap = sortParamKeys(params);
    String signature = sign(concatSignatureString(method, generateSortedSignature(treeMap)));
    // print(signature);
    return signature;
  }
}

