package com.rajeev.controller;

import com.rajeev.model.Request;
import com.rajeev.model.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/bot")
public class GPTController {

    @Value("${openai.model}")
    private String model;

    @Value(("${openai.api.url}"))
    private String apiURL;

    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/chat")
    public List<Response.Choice> chat(@RequestParam("prompt") String prompt){
        Request request=new Request(model, prompt);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return response.getChoices();//.get(0).getMessage().getContent();

//        http://localhost:8080/bot/chat?prompt=what is spring
    }

//    @GetMapping("/shayari")
//    public List<Response.Choice> shayariGeneratorHandler(@RequestParam("keyword") String keyword){
//        Request request=new Request(model, "Generate a 4 lines hindi shayari with the keyword: "+keyword);
//        Response response = restTemplate.postForObject(apiURL, request, Response.class);
//        return response.getChoices();//.get(0).getMessage().getContent();
//    }

    @GetMapping("/shayari")
    public ResponseEntity<String> shayariGeneratorHandler(@RequestParam("keyword") String keyword){
        Request request=new Request(model, "Generate a 4 lines hindi shayari with the keyword: "+keyword);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);

//        http://localhost:8080/bot/shayari?keyword=dil
    }

    @GetMapping("/quotes")
    public ResponseEntity<String> quotesGeneratorHandler(@RequestParam("topic") String topic){
        Request request=new Request(model, "Generate a quote on the topic : "+ topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @GetMapping("/jokes")
    public ResponseEntity<String> jokesGeneratorHandler(@RequestParam("topic") String topic){
        Request request=new Request(model, "Generate a funny joke on the topic : "+ topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @GetMapping("/stories")
    public ResponseEntity<String> storiesGeneratorHandler(@RequestParam("topic") String topic){
        Request request=new Request(model, "Generate a beautiful short story on the topic : "+ topic);
        Response response = restTemplate.postForObject(apiURL, request, Response.class);
        return new ResponseEntity<>(response.getChoices().get(0).getMessage().getContent(), HttpStatus.OK);
    }

    @GetMapping("/hello")
    public String hello(){
        return "hello world ";
    }
}


