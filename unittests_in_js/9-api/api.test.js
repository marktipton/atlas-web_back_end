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

// cart page tests
describe('Cart Page', function() {
  it('should return status code 200 when id is number', function(done) {
    chai.request('http://localhost:7865')
      .get('/cart/33')
      .end(function(error, response) {
        expect(response).to.have.status(200);
        expect(response.text).to.equal('Payment methods for cart 33');
        done();
      });
  });

  it('should return status code 404 when id is NaN', function(done) {
    chai.request('http://localhost:7865')
      .get('/cart/umhello?')
      .end(function(error, response) {
        expect(response).to.have.status(404);
        expect(response.text).to.equal('Id must be a number');
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
