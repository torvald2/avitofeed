
export async function GetAllPlatforms() {
  const resp = await fetch("/api/v1/platforms/");
  return await resp.json();
}
export async function NewPlatform(data) {
  const resp = await fetch("/api/v1/platforms/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return await resp.json();
}

export async function GetHierarcty(){
  const resp = await fetch("/api/v1/categories/?platform=1", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  return await resp.json();

}


export async function CreateEmptyCategory(platform) {
  const resp = await fetch("/api/v1/categories/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ 
                          "Platform": platform,
                           "Name":"Новая категория",
                           "Description":"Заполни меня ",
                           "XML_Value":"Cat",
                        
    })
  });
  
  return resp.status === 201
}