// const app = require('./api');
const chai = require('chai');
const expect = chai.expect;
const chaiHttp = require('chai-http');
chai.use(chaiHttp);

describe('Index Page', function() {
  it('should return status code 200', function(done) {
    chai.request('http://localhost:7865')
      .get('/')
      .end(function(error, response) {
        expect(response).to.have.status(200);
        done();
      });
  });

  it('should have content-type text/html', function(done) {
    chai.request('http://localhost:7865')
      .get('/')
      .end(function(error, response) {
        expect(response).to.have.header('content-type', 'text/html; charset=utf-8');
        done();
      });
  });

  it('should have correct return', function(done) {
    chai.request('http://localhost:7865')
      .get('/')
      .end(function(error, response) {
        expect(response.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
