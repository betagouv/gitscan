## Changelog : Aidants_Connect (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des mandats, notamment avec l'ajout de la génération d'attestations, la recherche de mandats expirés ou révoqués, et des améliorations de l'interface utilisateur. Des ajustements ont également été apportés pour clarifier l'orientation de l'application vers les professionnels et pour optimiser le processus d'inscription aux webinaires.

### Évolutions fonctionnelles
- **Mandats :**
    - Ajout de la possibilité de générer une attestation Aidants Connect. [#1754](https://github.com/betagouv/Aidants_Connect/issues/1754)
    - Ajout de la recherche de mandats expirés et révoqués. [#1739](https://github.com/betagouv/Aidants_Connect/issues/1739)
    - Ajout de cadres pour les signatures sur les mandats. [#1750](https://github.com/betagouv/Aidants_Connect/issues/1750)
    - Mise à jour du modèle de mandat (version 20260323) pour ajuster la taille du logo et améliorer la mise en page de l'attestation et des signatures.
- **Webinaires :**
    - Ajout d'un bouton d'action pour s'inscrire aux webinaires. [#1743](https://github.com/betagouv/Aidants_Connect/issues/1743)
    - Mise à jour des liens d'inscription aux webinaires. (plusieurs commits)
- **Référents :**
    - Ajout du numéro de téléphone dans le formulaire d'ajout d'un référent. [#1738](https://github.com/betagouv/Aidants_Connect/issues/1738)
- **Interface utilisateur :**
    - Clarification de l'orientation de l'application vers les professionnels dans l'en-tête et le pied de page. [#1760](https://github.com/betagouv/Aidants_Connect/issues/1760)
    - Correction d'une faute d'orthographe dans l'attestation. [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758)

### Évolutions techniques
- **CI/CD :** Ajout d'une vérification des migrations manquantes dans le pipeline CI. [#1734](https://github.com/betagouv/Aidants_Connect/issues/1734)
- **Tests :**
    - Ajout de tests pour l'API FNE et les filtres. [#1747](https://github.com/betagouv/Aidants_Connect/issues/1747)
    - Mise à jour des tests pour attendre que DSFR soit prêt au lieu de charger le document.
- **Dépendances :** Mise à jour de `django-filter` vers la version 26.1.0.
- **Notifications :** Les emails de notification pour les nouveaux aidants sont désormais envoyés uniquement aux administrateurs métier et super-administrateurs. [#1749](https://github.com/betagouv/Aidants_Connect/issues/1749)
- **Settings :** Changement de valeur par défaut dans les settings. [#1748](https://github.com/betagouv/Aidants_Connect/issues/1748)

### Autres changements
- Suppression de l'ancienne page Guide d'utilisation et redirection vers la nouvelle documentation. [#1746](https://github.com/betagouv/Aidants_Connect/issues/1746)
- Remise en place de la fonctionnalité de recherche dans la liste des mandats. [#1735](https://github.com/betagouv/Aidants_Connect/issues/1735)
- Ajout de valeurs dans le serializer FNE et de filtres. [#1742](https://github.com/betagouv/Aidants_Connect/issues/1742)
- Blocage de `setuptools` en dessous de la version 80.0. [#1737](https://github.com/betagouv/Aidants_Connect/issues/1737)
