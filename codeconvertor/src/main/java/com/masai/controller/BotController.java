package com.masai.controller;

import com.masai.model.QuoteRequest;
import com.masai.model.Request;
import com.masai.model.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/convertor")
public class BotController {
    @Value("${openai.model}")
    private String model;

    @Value(("${openai.api.url}"))
    private String apiURL;

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping("/hello")
    public String hello(){
        return "Please select any language first!";
    }

    @PostMapping("/java")
    public ResponseEntity<String> javaConverterHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Convert the given code into Java and write Main class if needed or haven't provided:  " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/python")
    public ResponseEntity<String> pythonConvertorHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Convert the given code into Python: " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/javascript")
    public ResponseEntity<String> javascriptConvertorHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Convert the given code into javascript: " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/csharp")
    public ResponseEntity<String> cSharpConvertorHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Convert the given code into C# and write Main class if needed or haven't provided:  " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/cplus")
    public ResponseEntity<String> cPlusConvertorHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Convert the given code into C++:" + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/debug")
    public ResponseEntity<String> debuggerHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Debug the given code and give me correct output: " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @PostMapping("/quality")
    public ResponseEntity<String> qualityHandler(@RequestBody QuoteRequest quoteRequest) {
        String topic = quoteRequest.getTopic();
        Request request = new Request(model, "Do a quality check for this code and give rating from 1 to 10 with appropriate suggestion: " + topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }
}
