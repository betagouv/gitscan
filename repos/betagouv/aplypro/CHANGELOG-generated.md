## Changelog : aplypro (30 derniers jours, au 8 juin 2026)

### Résumé
Cette version apporte des améliorations à l'affichage des informations sur les élèves, notamment les dates de scolarité et l'INE. Des corrections ont été apportées pour gérer les cas où ces informations sont manquantes. L'envoi des adresses redressées à l'ASP a été optimisé, et des améliorations ont été faites à la gestion des demandes de paiement et à la pagination des rapports.

### Évolutions fonctionnelles
- Affichage des dates de début et de fin de la scolarité dans l'espace académique. [#1970](https://github.com/betagouv/aplypro/issues/1970)
- Affichage d'un message clair lorsque l'élève n'a pas d'INE. [#1960](https://github.com/betagouv/aplypro/issues/1960)
- Modification des messages affichés pour les demandes de paiement afin de les rendre plus clairs. [#1967](https://github.com/betagouv/aplypro/issues/1967)
- Envoi de l'adresse redressée à l'ASP dès que l'élève a au moins une PFMP 'rectified'. [#1942](https://github.com/betagouv/aplypro/issues/1942)
- Correction de l'affichage lorsque la date de fin de scolarité est manquante. [#1972](https://github.com/betagouv/aplypro/issues/1972)

### Évolutions techniques
- Gestion améliorée des données 'rnvp_data' vides. [#1974](https://github.com/betagouv/aplypro/issues/1974)
- Extraction de la logique d'enrichissement des données dans un objet dédié pour une meilleure organisation du code.
- Pagination de la page d'index des rapports pour améliorer les performances. [#1956](https://github.com/betagouv/aplypro/issues/1956)
- Ajout d'une méthode `complete?` pour faciliter la vérification de l'état des données. [#1957](https://github.com/betagouv/aplypro/issues/1957)
- Modification du fichier d'intégration initial pour inclure les attributs d'adresse.
- Envoi par lot des corrections après l'intégration normale lors du traitement de l'intégration.

### Autres changements
- Corrections de style avec Rubocop. [#1963](https://github.com/betagouv/aplypro/issues/1963)
- Mise à jour des dépendances.
