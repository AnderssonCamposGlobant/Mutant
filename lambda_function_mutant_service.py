import json

def lambda_handler(event, context):
    
    permitidoA="AAAA"
    permitidoT="TTTT"
    permitidoC="CCCC"
    permitidoG="GGGG"
    
    print(event)
    jsonStr = json.dumps(event)
    jsonData = json.loads(jsonStr)
    print(jsonData)
    adn = jsonData["dna"]
    print(adn)
    
    horizontal0=adn[0]
    horizontal1=adn[1]
    horizontal2=adn[2]
    horizontal3=adn[3]
    horizontal4=adn[4]
    horizontal5=adn[5]

    vertical0 = horizontal0[0] + horizontal1[0] + horizontal2[0] + horizontal3[0] + horizontal4[0] + horizontal5[0]
    vertical1 = horizontal0[1] + horizontal1[1] + horizontal2[1] + horizontal3[1] + horizontal4[1] + horizontal5[1]
    vertical2 = horizontal0[2] + horizontal1[2] + horizontal2[2] + horizontal3[2] + horizontal4[2] + horizontal5[2]
    vertical3 = horizontal0[3] + horizontal1[3] + horizontal2[3] + horizontal3[3] + horizontal4[3] + horizontal5[3]
    vertical4 = horizontal0[4] + horizontal1[4] + horizontal2[4] + horizontal3[4] + horizontal4[4] + horizontal5[4]
    vertical5 = horizontal0[5] + horizontal1[5] + horizontal2[5] + horizontal3[5] + horizontal4[5] + horizontal5[5]

    diagonal0 = horizontal0[0] + horizontal1[1] + horizontal2[2] + horizontal3[3] + horizontal4[4] + horizontal5[5]
    diagonal1 = horizontal0[5] + horizontal1[4] + horizontal2[3] + horizontal3[2] + horizontal4[1] + horizontal5[0]

    app_response = {}
    app_response['message'] = 'No Eres un mutante' 
    
    response_object={}
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['statusCode']=403
    
    if permitidoA in horizontal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in horizontal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in horizontal2 : 
        app_response['message'] = 'Eres un mutante'
        response_object['statusCode']=200
        
    if permitidoA in horizontal3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in horizontal4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in horizontal5 : 
        app_response['message'] = 'Eres un mutante '
        response_object['statusCode']=200
    
    if permitidoT in horizontal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in horizontal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in horizontal2 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in horizontal3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in horizontal4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in horizontal5 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    
    if permitidoC in horizontal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in horizontal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in horizontal2 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in horizontal3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in horizontal4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in horizontal5 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    
    if permitidoG in horizontal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in horizontal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in horizontal2 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in horizontal3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in horizontal4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in horizontal5 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        

    if permitidoA in vertical0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in vertical1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in vertical2 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in vertical3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in vertical4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoA in vertical5 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    
    if permitidoT in vertical0  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in vertical1  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in vertical2  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in vertical3  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in vertical4  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in vertical5  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    
    if permitidoC in vertical0  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in vertical1  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in vertical2  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in vertical3  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in vertical4  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in vertical5  : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    
    if permitidoG in vertical0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in vertical1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in vertical2 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in vertical3 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in vertical4 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in vertical5 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        

    if permitidoA in diagonal0 : 
        app_response['message'] = 'Eres un mutante'  
        response_object['statusCode']=200
        
    if permitidoA in diagonal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in diagonal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoT in diagonal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in diagonal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoC in diagonal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in diagonal0 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    if permitidoG in diagonal1 : 
        app_response['message'] = 'Eres un mutante' 
        response_object['statusCode']=200
        
    response_object['body']=json.dumps(app_response)
    
    return response_object
