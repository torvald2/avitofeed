
export async function GetAllPlatforms(){
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

