## Changelog : portail-rse (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de la fonctionnalité d'exportation des données VSME au format PowerPoint (pptx). De nombreuses corrections et optimisations ont été apportées pour garantir un rendu précis et complet des informations, avec une gestion plus fine des indicateurs pertinents, non pertinents ou non applicables. Des améliorations ont également été apportées à l'administration et à la sécurité du portail.

### Évolutions fonctionnelles
- Ajout de la possibilité pour un utilisateur de réinitialiser un indicateur VSME. [#2a12381](https://github.com/betagouv/portail-rse/commit/2a12381)
- Amélioration de l'exportation des données VSME au format PPTX :
    - Ajout de la gestion des indicateurs non pertinents et non applicables, avec suppression des diapositives correspondantes ou affichage adapté.
    - Prise en charge de l'export de différents types de données (textes, nombres, tableaux, choix multiples).
    - Amélioration du style et de la mise en page des tableaux dans les présentations exportées.
    - Ajout de l'affichage des unités et des informations de l'entreprise sur la couverture.
    - Correction de bugs d'affichage et de formatage des données dans les présentations.
- Les exports PPTX sont maintenant disponibles via un lien protégé.
- Amélioration des boutons de téléchargement des rapports VSME.
- Possibilité de rechercher des utilisateurs par ensemble d'IDs dans l'administration. [#0b826a1](https://github.com/betagouv/portail-rse/commit/0b826a1)

### Évolutions techniques
- Mise à jour de la version de Django (5.1.15 vers 5.2.16). [#48eb2fc](https://github.com/betagouv/portail-rse/commit/48eb2fc)
- Mise à jour de la version de Node.js dans `package.json` et dans l'intégration continue. [#376ab90](https://github.com/betagouv/portail-rse/commit/376ab90)
- Refactoring du code lié à l'exportation PPTX pour améliorer la lisibilité et la maintenabilité.
- Nettoyage du code et suppression de définitions inutiles dans l'administration. [#8adeba0](https://github.com/betagouv/portail-rse/commit/8adeba0)
- Amélioration de la gestion des logs pour les requêtes d'export XLSX et PPTX. [#260e6ff](https://github.com/betagouv/portail-rse/commit/260e6ff)
- Correction d'une erreur potentielle de validation dans le calcul de certains champs. [#d167f46](https://github.com/betagouv/portail-rse/commit/d167f46)
- Correction du type d'un champ calculé dans la VSME. [#106119a](https://github.com/betagouv/portail-rse/commit/106119a)

### Autres changements
- Correction du label d'une colonne dans l'indicateur B7-38-c. [#effe076](https://github.com/betagouv/portail-rse/commit/effe076)
- Nettoyage du compte utilisateur de test pour les personnes sans compte Proconnect. [#f910a2b](https://github.com/betagouv/portail-rse/commit/f910a2b)
- Renommage de certaines commandes et méthodes pour une meilleure clarté. [#b5f630c](https://github.com/betagouv/portail-rse/commit/b5f630c) et [#8c5ae53](https://github.com/betagouv/portail-rse/commit/8c5ae53)
- Sécurisation de l'accès à la modification du profil et du mot de passe de l'utilisateur test. [#4df6290](https://github.com/betagouv/portail-rse/commit/4df6290) et [#42bcad5](https://github.com/betagouv/portail-rse/commit/42bcad5)
- Correction de l'export PPTX de l'indicateur C3-54-p2 dans certains cas. [#4d589ee](https://github.com/betagouv/portail-rse/commit/4d589ee)
- Mise à jour de la dépendance `joserfc` (1.6.7 -> 1.6.8 et 1.6.3 -> 1.6.7).
