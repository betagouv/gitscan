## Changelog : portail (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en matière de logging structuré pour faciliter le débogage et la surveillance. De plus, la gestion des backends dynamiques a été revue, permettant des mises à jour plus flexibles et dynamiques de la configuration. Des corrections et améliorations mineures ont également été apportées à la gestion des erreurs et aux tests.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémenté via les commits : `dac0437`, `b841bdc`, `6f51f9b`, `0f5be6c`, `0423b18`)
- Amélioration des informations retournées par l'API `ListBackends` pour une meilleure visibilité sur les backends disponibles.
- Correction d'un problème empêchant l'évaluation des ACLs pour le trafic UDP. [#5678](https://github.com/cloud-gouv/portail/issues/5678) (`0017f76`)
- Ajout de tests pour vérifier le timeout de connexion HTTP. (`f6e3dd0`, `dd169c1`)
- Amélioration de la gestion des erreurs côté client pour les requêtes HTTP, avec un retour plus précis des erreurs et une journalisation améliorée. (`9003a58`, `2fc2cf3`)

### Évolutions techniques
- Implémentation du logging structuré au format JSON pour le proxy, le serveur RPC et les composants associés. Cela inclut l'ajout d'IDs de trace pour faciliter le suivi des requêtes. (`b0c9b01`, `db7557f`, `7930872`, `f0f6ac1`, `fc152fe`, `859edc3`, `370796d`, `5a2043f`)
- Refonte de la configuration des règles ACL dans le module Nix pour utiliser une structure basée sur des attributs. (`d9cf054`)
- Amélioration de la gestion des erreurs et de la journalisation dans le code RPC. (`a0786d2`, `b7d79e7`, `f13f201`, `e6c57eb`)
- Utilisation de `request-timeout` pour gérer les timeouts de connexion et les tentatives de backend HTTP. (`dd169c1`)
- Refactorisation du contexte du proxy pour une meilleure gestion des informations de routage. (`29a2e96`, `c7287f5`, `1480347`, `db7557f`)

### Autres changements
- Mise à jour de plusieurs dépendances Rust (uuid, anyhow, bytes, regex, rustls-pki-types).
- Mise à jour des actions GitHub (actions/checkout).
- Amélioration de la configuration du workflow CI/CD pour exécuter tous les jobs en parallèle. (`c2618a8`)
- Correction de quelques fautes de frappe dans les messages d'erreur RPC. (`0423b18`)
- Changement du type de pointeur pour assurer la compatibilité multiplateforme. (`a4e3901`)
- Déplacement du socket RPC dans un répertoire dédié. (`c30347d`)
