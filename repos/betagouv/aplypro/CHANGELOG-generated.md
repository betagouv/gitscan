## Changelog : aplypro (30 derniers jours, au 8 juin 2026)

### Résumé
Cette version apporte des améliorations à l'affichage des informations sur les élèves (dates de scolarité, INE) et des demandes de paiement. Des corrections de bugs ont été implémentées pour l'affichage des dates de fin de scolarité et la gestion des données d'adresse. L'intégration avec l'ASP a été optimisée pour l'envoi des adresses redressées. Enfin, la pagination des rapports a été ajoutée pour améliorer la performance.

### Évolutions fonctionnelles
- Affichage de la date de début et de fin de la scolarité dans l'espace académique. [#1970](https://github.com/betagouv/aplypro/issues/1970)
- Affichage d'un message clair lorsque l'élève n'a pas d'INE. [#1960](https://github.com/betagouv/aplypro/issues/1960)
- Modification des messages affichés pour les demandes de paiement pour une meilleure clarté. [#1967](https://github.com/betagouv/aplypro/issues/1967)
- Envoi de l'adresse redressée à l'ASP dès que l'élève a au moins une PFMP 'rectified'. [#1942](https://github.com/betagouv/aplypro/issues/1942)

### Évolutions techniques
- Pagination de la page d'index des rapports pour améliorer les performances. [#1956](https://github.com/betagouv/aplypro/issues/1956)
- Extraction de la logique d'enrichissement des données dans un objet dédié pour une meilleure organisation du code. [#1957](https://github.com/betagouv/aplypro/issues/1957)
- Modification du fichier d'intégration initial pour inclure les attributs d'adresse. [#1956](https://github.com/betagouv/aplypro/issues/1956)
- Envoi par lot des corrections après l'intégration normale lors du traitement de l'intégration.

### Autres changements
- Correction d'un bug d'affichage pour la date de fin de scolarité manquante. [#1972](https://github.com/betagouv/aplypro/issues/1972)
- Gestion des cas où `rnvp_data` est vide. [#1974](https://github.com/betagouv/aplypro/issues/1974)
- Corrections Rubocop pour améliorer la qualité du code.
- Mise à jour du bundle.
