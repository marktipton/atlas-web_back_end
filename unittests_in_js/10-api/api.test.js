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

// Tests for available_payments
describe('Available Payments', function() {
  it('should return status code 200 and correct structure', function(done) {
    chai.request('http://localhost:7865')
      .get('/available_payments')
      .end(function(error, response) {
        expect(response).to.have.status(200);
        expect(response.body).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
        done();
      });
  });
});

// Tests for login post endpoint
describe('Login', function() {
  it('should return status code 200 and welcome message', function(done) {
    chai.request('http://localhost:7865')
      .post('/login')
      .send({ userName: 'John' })
      .end(function(error, response) {
        expect(response).to.have.status(200);
        expect(response.text).to.equal('Welcome John');
        done();
      });
  });

  it('should return status code 400 when userName is missing', function(done) {
    chai.request('http://localhost:7865')
      .post('/login')
      .send({})
      .end(function(error, response) {
        expect(response).to.have.status(400);
        expect(response.text).to.equal('Missing userName');
        done();
      });
  });
});