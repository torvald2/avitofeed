
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

export async function GetHierarcty(hier){
  let  url = `/api/v1/categories/`
  if (hier){
     url = `/api/v1/categories/?platform=${hier}`
  }
  const resp = await fetch(url, {
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


export async function DeleteCategory(cat_id) {
  const resp = await fetch(`/api/v1/categories/?id=${cat_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
   
  });
  
  return resp.status === 204
}



export async function UpdateCategory(cat_id, parent, name, desc, XML_Value, table) {
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
}
