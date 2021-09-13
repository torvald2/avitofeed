
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

export async function CreateEmptyChildCategory(platform, parent) {
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
                           "Parent":parent
                        
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

export async function DeletePlatform(platform_id) {
  const resp = await fetch(`/api/v1/platforms/?id=${platform_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
   
  });
  
  return resp.status === 204
}



export async function UpdateCategory(cat_id, parent, name, desc, XML_Value, table, platform) {
  const resp = await fetch(`/api/v1/categories/?id=${cat_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ 
                          "Platform": platform,
                           "Name":name,
                           "Description":desc,
                           "XML_Value":XML_Value,
                           "Parent":parent,
                           "Table":table
                        
    })
  });
  return resp.status === 200
}


export async function GetTables(platform){
  let  url = `/api/v1/tables/`
  if (platform){
     url = `/api/v1/tables/?platform=${platform}`
  }
  const resp = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  return await resp.json();

}


export async function NewTable(name,platform) {
  const resp = await fetch("/api/v1/tables/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({"name":name, "platform":platform}),
  });
  return resp.status ===201
}

export async function DeleteTable(cat_id) {
  const resp = await fetch(`/api/v1/tables/?id=${cat_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
   
  });
  
  return resp.status === 204
}

export async function GetCells(table){
  let  url = `/api/v1/cells/`
  if (table){
     url = `/api/v1/cells/?platform=${table}`
  }
  const resp = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  return await resp.json();

}

export async function NewCel(tableId) {
  const resp = await fetch("/api/v1/cells/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      table: tableId,
      cellName: "Новое поле",
      info: "Отредактируй меня",
      xmlValue:"cell",
      dataType:1,
      values:["0"],
      max_len:1,
    }),
  });
  return resp.status ===201
}

export async function SaveCell(data) {
  const resp = await fetch(`/api/v1/cells/?id=${data.id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
  });
  return resp.status === 200
}