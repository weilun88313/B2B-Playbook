import assert from "node:assert/strict";
import test from "node:test";

import { scoreAccount } from "./icp-account-scorer.mjs";

test("classifies a strong account with a trigger as T1", () => {
  const result = scoreAccount({
    name: "Strong account",
    useCase: 2,
    budget: 2,
    alternative: 2,
    trigger: 1,
    committee: 1,
  });

  assert.equal(result.total, 8);
  assert.equal(result.tier, "T1");
  assert.equal(result.triggerGatePassed, true);
});

test("caps a high-fit account without a trigger at T2", () => {
  const result = scoreAccount({
    name: "No trigger",
    useCase: 2,
    budget: 2,
    alternative: 2,
    trigger: 0,
    committee: 2,
  });

  assert.equal(result.total, 8);
  assert.equal(result.tier, "T2");
  assert.equal(result.triggerGatePassed, false);
});

test("a hard disqualifier always results in T3", () => {
  const result = scoreAccount({
    name: "Disqualified",
    useCase: 2,
    budget: 2,
    alternative: 2,
    trigger: 2,
    committee: 2,
    disqualified: "No purchasing function",
  });

  assert.equal(result.total, 10);
  assert.equal(result.tier, "T3");
});

test("rejects scores outside the 0–2 scale", () => {
  assert.throws(
    () =>
      scoreAccount({
        name: "Invalid",
        useCase: 3,
        budget: 0,
        alternative: 0,
        trigger: 0,
        committee: 0,
      }),
    /must be 0, 1, or 2/,
  );
});
