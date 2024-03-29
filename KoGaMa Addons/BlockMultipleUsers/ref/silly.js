const CLIENT_ID = SELFID;
const PROFILE_IDS = [
  1186442,
  2416361,
  2814866,
  51597483,
  10183579,
  18365116,
  18515594,
  19531003,
  20037522,
  20107599,
  21269335,
  23213484,
  24304847,
  50417643,
  50709102,
  51605152,
  667411050,
  667630286,
  667789126,
  667834566,
  668124616,
  668156150,
  668303247,
  668332488,
  669107441,
  669358563,
  669537156,
  669605680,
  669730391,
  25037907,
  669537156,
  18838122,
  668602201,
  14852072,
  24388642,
  22810749,
  10828824,
  18542003,
  50415149,
  669876853,
  23102454,
  12286005,
  666971177,
  668247871,
  50414365,
  668699435,
  16729673,
  25463983,
  22797063,
  50034220,
  4021631,
  16721464,
  8637137,
  18101371,
  668428904,
  16873893,
  19531003,
  19985209,
  21421861,
  9610391,
  17037147,
  2814866,
  668301622,
  25453113,
  19222931,
  21269335,
  23213484,
  667171407,
  22845155,
  667844506
];


async function blockUserWithDelay(profileId, delay) {
  await new Promise((resolve) => setTimeout(resolve, delay));

  const response = await fetch(`/user/${CLIENT_ID}/block/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "X-Csrf-Token": ""
    },
    body: JSON.stringify({
      profile_id: profileId
    })
  });

  if (response.ok) {
    console.log(`%cBlocked user with profile ID: ${profileId}`, "color: #f0bb2b");
  }
}


async function blockMultipleUsersWithDelay() {
  const delayBetweenRequests = 2000; 

  for (const profileId of PROFILE_IDS) {
    await blockUserWithDelay(profileId, delayBetweenRequests);
  }

  console.log("%cAll users have been blocked.", "color: #6f98b0");
}


blockMultipleUsersWithDelay();