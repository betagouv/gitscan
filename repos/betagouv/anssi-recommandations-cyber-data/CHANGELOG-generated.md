## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la gestion des collections de documents et l'expérience utilisateur. Des correctifs ont été apportés pour améliorer la sécurité du pipeline CI/CD, permettre la suppression de documents, et faciliter la gestion des collections via l'interface utilisateur. Des mises à jour de dépendances ont également été effectuées pour corriger des vulnérabilités et bénéficier des dernières améliorations.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des documents. [#72ae2e6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/72ae2e6)
- Ajout d'un formulaire permettant de supprimer (jeopardyser) une collection entière de documents. [#b14126a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b14126a)
- Ajout d'un formulaire pour sélectionner les collections à récupérer depuis le client Albert. [#5787f18](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/5787f18)
- Possibilité de récupérer les collections désirées via la route GET /collections. [#271da19](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/271da19)
- Ajout de la possibilité d'ajouter un document HTML depuis une URL. [#e47f117](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/e47f117)
- Ajout du champ URL du document. [#5007f36](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/5007f36)
- Redirection vers le TDB (Tooling DataBase) après authentification. [#f2ab570](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f2ab570)
- Correction de l'enrôlement en fournissant le bon nom d'utilisateur. [#0f94d12](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/0f94d12)

### Évolutions techniques
- Mise à jour de Docling vers une version >= 2.97.0 pour des raisons de sécurité. [#a8d9e8e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a8d9e8e)
- Ajout de `zizmor` pour valider la configuration et améliorer la sécurité. [#685a93e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/685a93e)
- Désactivation des identifiants `git` des dépôts clonés dans le pipeline CI/CD pour renforcer la sécurité. [#94041bd](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/94041bd)
- Extraction d'un composant `PageInformationsCollections` pour une meilleure organisation du code. [#acf723a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/acf723a)
- Correction de l'encodage des noms de documents en UTF-8. [#cece025](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/cece025)

### Autres changements
- Ajout de l'action Renovate pour la gestion automatisée des dépendances. [#19f167b](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/19f167b)
- Mise à jour de nombreuses dépendances (eslint, prettier, tailwindcss, vitest, etc.) via Renovate. Ces mises à jour incluent des corrections de sécurité et des améliorations de performance.
- Modification du prompt pour réduire les hallucinations. [#f24d3b4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f24d3b4)
- Correction de format. [#25d57b7](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/25d57b7)
