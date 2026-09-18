import Lake
open Lake DSL

package "beal" where
  version := v!"0.1.0"
  keywords := #["math", "number-theory", "beal-conjecture", "formal-verification"]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.14.0"

@[default_target]
lean_lib «Beal» where
  roots := #[`Beal]
