const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    createProxyMiddleware("/v1/db", {
      target: "https://rqkaoaapxc.execute-api.ap-northeast-1.amazonaws.com/", //타겟이 되는 api url를 입력
      changeOrigin: true, //대상 서버 구성에 따라 호스트 헤더가 변경되도록 설정하는 부분
    })
  );
};
