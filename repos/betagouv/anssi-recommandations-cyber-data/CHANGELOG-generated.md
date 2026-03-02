## Changelog : anssi-recommandations-cyber-data (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la refactorisation du code pour une meilleure maintenabilité et l'ajout de fonctionnalités pour faciliter l'indexation de différents types de documents (PDF et JSON) et leur intégration avec Albert. Des corrections de bugs ont également été apportées pour améliorer la fiabilité du système, notamment lors de la création de collections et des appels à MQC.

### Évolutions fonctionnelles
- Possibilité d'ajouter un seul document à une collection existante. [#14966f0](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/14966f0)
- Ajout de la possibilité de transmettre un fichier JSON pour l'indexation. [#f0a200d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/f0a200d)
- Ajout d'options spécifiques pour le document `anssi-fondamentaux-securisation-poste-multi-environnements-v1-0.pdf`. [#60048f4](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/60048f4)
- Modification de la collection d'un PDF pour spécifier le fichier. [#fc09c5d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/fc09c5d)
- Ajout d'un adaptateur `ClientAlbert` pour faciliter l'intégration avec Albert. [#14966f0](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/14966f0)

### Évolutions techniques
- Refactorisation du code pour extraire un générateur de page et une abstraction de `Page` avec une implémentation `PagPDF`, améliorant ainsi la structure et la maintenabilité du code. [#b90d373](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/b90d373), [#1b4f703](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1b4f703)
- Extraction d'une classe `DocumentAIndexer` pour faciliter l'ajout de nouveaux types de documents (HTML par exemple). [#29c3a3a](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/29c3a3a)
- Suppression du chunker Docling hiérarchique inutilisé. [#1b72e26](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/1b72e26)
- Correction de la valeur du type utilisateur envoyé à MQC et ajout du type utilisateur `EVALUATION` lors de l'appel à MQC. [#e8b3881](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/e8b3881), [#a30eea0](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/a30eea0)
- Correction d'un bug lors de l'exécution des requêtes lors de la création d'une collection. [#6b324b3](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/6b324b3)

### Autres changements
- Mise à jour de `deepeval` et `protobuf` suite à une alerte de sécurité Dependabot. [#45e637e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/45e637e)
- Suppression de la dépendance obsolète `canvas`. [#8b15b9c](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/8b15b9c)
- Renommage de `guide` en `document` et de `document_pdf` en `document_a_indexer` pour une meilleure clarté du code. [#73daa42](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/73daa42), [#5c1aa5d](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/5c1aa5d)
- Extraction de la fonction `cree_document_pdf` et déplacement de `collecte_document_pdf` dans son script. [#d328a5c](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/d328a5c)
