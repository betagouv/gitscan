## Changelog : mobilic (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface d'administration, notamment la page d'accueil avec de nouvelles informations et une meilleure présentation des données. Des améliorations ont également été apportées à la recherche NATINF, à la gestion des véhicules et à la sécurité avec l'ajout de l'authentification à deux facteurs (2FA). Plusieurs corrections de bugs et optimisations ont été réalisées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de recherche NATINF [#842](https://github.com/MTES-MCT/mobilic/pulls/842).
- Refonte de la page d'accueil de l'administration avec de nouvelles informations et une meilleure présentation des données [#836](https://github.com/MTES-MCT/mobilic/pulls/836).
- Implémentation de l'importation en masse de véhicules dans l'administration [#837](https://github.com/MTES-MCT/mobilic/pulls/837).
- Ajout d'un support pour l'administration back-office [#826](https://github.com/MTES-MCT/mobilic/pulls/826).
- Ajout de la possibilité de supprimer les infractions NATINF avec une confirmation modale.
- Ajout de l'authentification à deux facteurs (2FA) avec support de l'impersonation d'utilisateurs.
- Amélioration de l'expérience utilisateur lors de l'édition des infractions dans l'interface de contrôle.
- Ajout du logo Chaventon Express [#848](https://github.com/MTES-MCT/mobilic/pulls/848).

### Évolutions techniques
- Refactorisation de composants pour améliorer la réutilisabilité et la maintenabilité du code.
- Remplacement des icônes Material-UI par des icônes DSFR dans les composants d'infraction.
- Utilisation de composants DSFR pour améliorer la cohérence visuelle et l'accessibilité.
- Extraction de constantes et de logiques partagées pour simplifier le code et éviter les duplications.
- Amélioration de la validation des numéros d'immatriculation des véhicules.
- Correction de problèmes de performance et de stabilité.
- Mise à jour de la documentation et des tests.

### Autres changements
- Mise à jour du texte de la page de sécurité [#850](https://github.com/MTES-MCT/mobilic/pulls/850).
- Correction de fautes de frappe et d'erreurs de typographie.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de variables et d'imports inutilisés.
- Correction de problèmes de style et d'alignement.
- Correction de problèmes liés au rafraîchissement des données après la validation d'une mission [#854](https://github.com/MTES-MCT/mobilic/pulls/854).
- Correction de l'affichage des jours de travail après la validation d'une mission.
- Amélioration de la gestion des erreurs lors de la déconnexion pendant l'impersonation.
- Correction de l'affichage des infractions multi-employeurs sur la page d'accueil de l'administration.
- Correction de l'affichage des jours non respectés sur la page d'accueil de l'administration.
