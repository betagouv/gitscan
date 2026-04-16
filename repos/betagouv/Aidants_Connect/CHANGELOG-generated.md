## Changelog : Aidants_Connect (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, Aidants Connect a connu des améliorations significatives concernant la gestion des mandats, notamment l'ajout de la génération d'attestations, la recherche de mandats expirés ou révoqués, et des préparatifs pour la gestion des demandes de changement de structure. Des ajustements ont également été apportés à l'interface utilisateur et aux notifications pour une meilleure expérience utilisateur et une administration plus précise.

### Évolutions fonctionnelles
- **Mandats :**
    - Ajout de la possibilité de générer une attestation Aidants Connect. [#1754](https://github.com/betagouv/Aidants_Connect/issues/1754)
    - Possibilité de rechercher les mandats expirés et révoqués. [#1739](https://github.com/betagouv/Aidants_Connect/issues/1739)
    - Ajout de cadres pour les signatures sur les mandats. [#1750](https://github.com/betagouv/Aidants_Connect/issues/1750)
    - Mise à jour du modèle de mandat pour la version 20260323, améliorant la mise en page et l'affichage des signatures.
- **Formations :**
    - Possibilité de contrôler la publication ou non des formations. [#1759](https://github.com/betagouv/Aidants_Connect/issues/1759)
- **Référents :**
    - Ajout du numéro de téléphone dans le formulaire d'ajout d'un référent. [#1738](https://github.com/betagouv/Aidants_Connect/issues/1738)
- **Notifications :**
    - Les notifications de nouveaux aidants sont désormais envoyées uniquement aux administrateurs métier et super-administrateurs. [#1749](https://github.com/betagouv/Aidants_Connect/issues/1749)
- **Interface utilisateur :**
    - Mise à jour de l'en-tête et du pied de page pour clarifier que Aidants Connect s'adresse aux professionnels. [#1760](https://github.com/betagouv/Aidants_Connect/issues/1760)
    - Suppression de l'ancienne page "Guide d'utilisation" et redirection vers la nouvelle documentation. [#1746](https://github.com/betagouv/Aidants_Connect/issues/1746)
    - Ajout d'un bouton d'action pour s'inscrire au webinaire et faire une demande d'habilitation. [#1743](https://github.com/betagouv/Aidants_Connect/issues/1743)
    - Correction d'une faute d'orthographe dans l'attestation. [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758)
    - Remise en place de la fonctionnalité de recherche dans la liste des mandats. [#1735](https://github.com/betagouv/Aidants_Connect/issues/1735)

### Évolutions techniques
- **CI/CD :** Ajout d'une vérification des migrations manquantes dans le pipeline CI. [#1734](https://github.com/betagouv/Aidants_Connect/issues/1734)
- **Modèle de données :** Création du modèle de données pour les demandes de changement de structure. [#1732](https://github.com/betagouv/Aidants_Connect/issues/1732)
- **Dépendances :** Mise à jour de la librairie `django-filter` en version 26.1.0.
- **Tests :** Ajout de tests pour l'API FNE et les filtres. [#1747](https://github.com/betagouv/Aidants_Connect/issues/1747)
- **Configuration :** Changement de valeurs par défaut dans les settings. [#1748](https://github.com/betagouv/Aidants_Connect/issues/1748)

### Autres changements
- Correction du balisage du fieldset de demande d'habilitation. [#1733](https://github.com/betagouv/Aidants_Connect/issues/1733)
- Amélioration des tests pour attendre la disponibilité de DSFR au lieu du chargement du document.
- Diverses corrections et améliorations mineures.
