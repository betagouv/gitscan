## Changelog : resorption-bidonvilles (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration des indicateurs de suivi des actions, notamment en intégrant des données de financement DIHAL et en affichant des informations plus précises sur la mise à jour des données. Des corrections et améliorations ont également été apportées à l'interface utilisateur et à la gestion des accès.

### Évolutions fonctionnelles
- Ajout d'indicateurs de mise à jour de la population affichés dans l'email récapitulatif hebdomadaire.
- Affichage des indicateurs de mise à jour de population sur 3 mois.
- Ajout du champ "année de financement DIHAL" pour filtrer les actions.
- Affichage de l'année de financement DIHAL dans un badge.
- Ajout de l'adresse email du demandeur d'accès lors d'une demande.
- Correction du lien de demande d'information pour une demande d'accès.
- Ajout d'une popup pour l'export des actions.
- Ajout des statistiques de sites financés par DIHAL.
- Correction de la formulation des taux de mises à jour.

### Évolutions techniques
- Refactorisation de l'accès à Matomo pour utiliser un lien proxifié.
- Simplification de l'appel à une action factice (fakeAction).
- Amélioration du test unitaire associé.
- Mutualisation du code pour les opérations d'import/export de seeders.
- Utilisation de la version mutualisée des JSON pour les seeders.
- Extraction des utilitaires d'affichage des badges de statistiques.
- Sécurisation et transmission des données pour le header des actions.
- Intégration du header des actions avec le taux calculé.
- Correction de l'expiration du jeton d'activation (passée de 10 minutes à 168 heures).

### Autres changements
- Correction de plusieurs erreurs de linting.
- Amélioration de l'affichage du département dans l'onglet "tous".
- Amélioration du score du code.
- DSFRisation de l'affichage de l'erreur d'export.
- Correction de la hauteur de la popup.
- Renommage d'un fichier image.
- Correction de problèmes liés au clic et à la gestion des événements.
- Correction de l'affichage de la date.
- Correction de plusieurs erreurs de typage.
