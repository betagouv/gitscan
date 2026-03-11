## Changelog : openbao (30 derniers jours)

### Résumé
Les dernières mises à jour d'OpenBao incluent des corrections de sécurité importantes, des améliorations de la stabilité et de la gestion des montages, ainsi que des optimisations internes et des mises à jour de dépendances. Des améliorations de la documentation et des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur et la fiabilité du système.

### Évolutions fonctionnelles
- Correction d'un problème où l'auto-déverrouillage échouait lors de la mise à niveau vers v2.5.0 ou de la rétrogradation vers une version antérieure, affectant plusieurs fournisseurs KMS. [#2505](https://github.com/cloud-gouv/openbao/pull/2505)
- Correction d'un problème où le nombre total de baux n'était pas décrémenté lors de la révocation de baux irrévocables. [#2414](https://github.com/cloud-gouv/openbao/pull/2414)
- Correction d'un problème de "contexte annulé" dans le traitement de l'invalidation du cache PKI, qui provoquait des erreurs 500. [#2472](https://github.com/cloud-gouv/openbao/pull/2472)
- Ajout de VaultCourier aux bibliothèques clientes communautaires. [#2513](https://github.com/cloud-gouv/openbao/pull/2513)
- Correction du texte d'aide de l'interface de ligne de commande pour remplacer "Vault" par "OpenBao". [#2526](https://github.com/cloud-gouv/openbao/pull/2526)
- Ajout d'un paramètre hash dans la documentation. [#2474](https://github.com/cloud-gouv/openbao/pull/2474)
- Suppression d'anciennes informations concernant la désactivation de l'interface utilisateur dans la documentation. [#2475](https://github.com/cloud-gouv/openbao/pull/2475)

### Évolutions techniques
- Mise à jour vers Go 1.25.7 pour corriger une vulnérabilité de sécurité (CVE-2025-68121 / GO-2026-4337).
- Mise à jour de la bibliothèque `go.opentelemetry.io/otel/sdk` vers la version 1.40.0 pour corriger des vulnérabilités de sécurité (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- Suppression des montages de groupes d'identité corrompus pré-v2.5.0 lors du déverrouillage. [#2454](https://github.com/cloud-gouv/openbao/pull/2454)
- Refactorisation du code pour améliorer la structure et la maintenabilité.
  - Déplacement de `/internalshared` vers `/helper`. [#2449](https://github.com/cloud-gouv/openbao/pull/2449)
  - Refactorisation du code de la barrière dans son propre package. [#2425](https://github.com/cloud-gouv/openbao/pull/2425)
- Amélioration de la gestion des erreurs et de la robustesse du code.
  - Correction de plusieurs erreurs non gérées. [#2229](https://github.com/cloud-gouv/openbao/pull/2229)
  - Correction de problèmes liés à l'initialisation parallèle de PostgreSQL. [#2195](https://github.com/cloud-gouv/openbao/pull/2195)
- Utilisation de chemins absolus dans le fichier `CODEOWNERS`. [#2528](https://github.com/cloud-gouv/openbao/pull/2528)
- Ajout de tests de complexité cyclomatique avec le linter Cyclop. [#2423](https://github.com/cloud-gouv/openbao/pull/2423)

### Autres changements
- Mise à jour de diverses dépendances :
  - `goreleaser/goreleaser-action` (6.4.0 -> 7.0.0) [#2516](https://github.com/cloud-gouv/openbao/pull/2516)
  - `github.com/mholt/acmez/v3` (3.1.4 -> 3.1.5) [#2522](https://github.com/cloud-gouv/openbao/pull/2522)
  - `@easyops-cn/docusaurus-search-local` [#2515](https://github.com/cloud-gouv/openbao/pull/2515)
  - `k8s.io/client-go` (0.35.0 -> 0.35.1) [#2520](https://github.com/cloud-gouv/openbao/pull/2520)
  - `golang.org/x/sys` (0.40.0 -> 0.41.0) [#2517](https://github.com/cloud-gouv/openbao/pull/2517)
  - `google.golang.org/api` (0.264.0 -> 0.265.0) [#2524](https://github.com/cloud-gouv/openbao/pull/2524)
  - `go.opentelemetry.io/otel/sdk` (1.39.0 -> 1.40.0) [#2518](https://github.com/cloud-gouv/openbao/pull/2518)
  - `anchore/sbom-action` (0.22.1 -> 0.22.2) [#2482](https://github.com/cloud-gouv/openbao/pull/2482)
  - `github.com/google/cel-go` (0.26.1 -> 0.27.0) [#2481](https://github.com/cloud-gouv/openbao/pull/2481)
  - `k8s.io/apimachinery` (0.35.0 -> 0.35.1) [#2484](https://github.com/cloud-gouv/openbao/pull/2484)
  - `github.com/coreos/go-systemd/v22` (22.6.0 -> 22.7.0) [#2483](https://github.com/cloud-gouv/openbao/pull/2483)
  - `github.com/pires/go-proxyproto` (0.9.1 -> 0.9.2) [#2480](https://github.com/cloud-gouv/openbao/pull/2480)
  - `github.com/shirou/gopsutil/v4` (4.25.12 -> 4.26.1) [#2479](https://github.com/cloud-gouv/openbao/pull/2479)
  - `github.com/klauspost/compress` (1.18.3 -> 1.18.4) [#2478](https://github.com/cloud-gouv/openbao/pull/2478)
  - `yarn` [#2457](https://github.com/cloud-gouv/openbao/pull/2457)
- Mise à jour des membres du TSC et des entrées correspondantes. [#2486](https://github.com/cloud-gouv/openbao/pull/2486)
- Ajout des permissions de committer core et openbao-plugins à Philipp. [#2487](https://github.com/cloud-gouv/openbao/pull/2487)
- Mise à jour des informations du calendrier. [#2488](https://github.com/cloud-gouv/openbao/pull/2488)
- Suppression de Philipp Stehle de la liste des modérateurs au niveau de l'organisation. [#2489](https://github.com/cloud-gouv/openbao/pull/2489)
