## Changelog : anssi-recommandations-cyber-data (30 derniers jours)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'indexation des documents, en particulier des PDF, et sur la préparation de l'intégration de documents HTML. Des refactorings importants ont été effectués pour rendre le code plus modulaire et maintenable, facilitant ainsi l'ajout de nouvelles fonctionnalités et l'amélioration de la gestion des documents. Des corrections de bugs ont également été apportées pour améliorer la fiabilité du système.

### Évolutions fonctionnelles
- Possibilité de spécifier un fichier PDF lors de la création d'une collection. [#fc09c5d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/fc09c5d)
- Ajout de la prise en charge de la transmission d'un fichier JSON. [#f0a200d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f0a200d)
- Ajout des options pour le document `anssi-fondamentaux-securisation-poste-multi-environnements-v1-0.pdf`. [#60048f4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/60048f4)
- Correction d'un bug lors de la création d'une collection, améliorant la fiabilité du processus. [#6b324b3](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6b324b3)

### Évolutions techniques
- Refactorisation majeure du package d'indexation des documents pour une meilleure organisation et maintenabilité. [#2f8604d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/2f8604d)
- Extraction d'une abstraction `DocumentAIndexer` pour faciliter l'intégration de nouveaux types de documents (HTML). [#29c3a3a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/29c3a3a)
- Création d'une abstraction `Page` avec une implémentation `PagePDF` pour une meilleure gestion des pages PDF. [#1b4f703](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1b4f703)
- Déplacement de la gestion des documents PDF dans un package dédié `documents/pdf`. [#9b22a4b](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/9b22a4b)
- Génération des pages directement depuis le document pour une meilleure performance. [#135b765](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/135b765)
- Extraction d'un générateur de page pour une meilleure réutilisabilité. [#b90d373](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b90d373)
- Correction de la valeur du type utilisateur envoyé à MQC pour une meilleure intégration. [#e8b3881](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/e8b3881)
- Ajout du type utilisateur `EVALUATION` lors de l’appel à MQC. [#a30eea0](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a30eea0)

### Autres changements
- Mise à jour de `deepeval` et `protobuf` suite à une alerte de sécurité dependabot. [#45e637e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/45e637e)
- Fourniture du fichier servant la liste des documents distants à intégrer. [#88b18f6](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/88b18f6)
- Suppression de méthodes et de fixtures inutiles pour nettoyer le code. [#9c93f01](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/9c93f01), [#1586927](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1586927), [#58c64e8](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/58c64e8)
- Passage de certains champs de `DocumePDF` en privé. [#ec591e5](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/ec591e5)
- Renommage de `guide` en `document` pour une meilleure cohérence. [#73daa42](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/73daa42)
- Suppression du chunker docling hierarchique. [#1b72e26](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1b72e26)
- Extraction de la fonction `cree_document_pdf` et déplacement de `collecte_document_pdf` dans son script. [#d328a5c](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/d328a5c)
