## Changelog : monitorenv (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, l'application monitorenv a bénéficié d'améliorations significatives de l'interface utilisateur, notamment concernant la gestion des zones réglementaires, des zones de vigilance et des AMP (aires marines protégées). Des corrections de bugs et des optimisations ont également été apportées, en particulier au niveau des données et de l'authentification. Des améliorations techniques ont été réalisées pour la gestion des dépendances et la robustesse du code.

### Évolutions fonctionnelles

- **Zones réglementaires :**
    - Correction du tri des zones réglementaires par façade maritime. [#c25727b](https://github.com/MTES-MCT/monitorenv/commit/c25727b)
    - Amélioration du formulaire de modification des zones réglementaires.
    - Mise en évidence des zones réglementaires récentes ou mises à jour.
- **Zones de vigilance :**
    - Ajout d'un filtre pour afficher les zones de vigilance récentes. [#405b92e](https://github.com/MTES-MCT/monitorenv/commit/405b92e)
    - Mise à jour de l'icône et du tri par date de création par défaut. [#ad07290](https://github.com/MTES-MCT/monitorenv/commit/ad07290)
    - Nouvelle table avec des lignes extensibles pour une meilleure visualisation. [#6430d0f](https://github.com/MTES-MCT/monitorenv/commit/6430d0f)
    - Ajout de colonnes épinglées pour une meilleure lisibilité. [#207f6a8](https://github.com/MTES-MCT/monitorenv/commit/207f6a8)
    - Mise à jour des filtres dans la vue de liste. [#3795f40](https://github.com/MTES-MCT/monitorenv/commit/3795f40)
- **AMP (Aires Marines Protégées) :**
    - Mise en évidence des nouvelles AMP. [#eed0ba0](https://github.com/MTES-MCT/monitorenv/commit/eed0ba0)
    - Correction du flux de données des AMP. [#dd1f770](https://github.com/MTES-MCT/monitorenv/commit/dd1f770)
    - Mise en évidence des AMP et des zones réglementaires épinglées. [#882d0bc](https://github.com/MTES-MCT/monitorenv/commit/882d0bc)
- **Vaisseaux :**
    - Ajout du tonnage brut UMS aux informations du navire. [#a3ed217](https://github.com/MTES-MCT/monitorenv/commit/a3ed217)
- **Authentification :**
    - Vérification de la présence de la revendication "organizational_unit" pour renforcer la sécurité. [#1608c9c](https://github.com/MTES-MCT/monitorenv/commit/1608c9c)

### Évolutions techniques

- **Base de données :**
    - Ajout d'un index sur les données d'identification pour améliorer les performances. [#eb8cb9d](https://github.com/MTES-MCT/monitorenv/commit/eb8cb9d)
- **Gestion des dépendances :**
    - Configuration de dependabot pour des mises à jour moins fréquentes (cooldown de 30 jours). [#ca95117](https://github.com/MTES-MCT/monitorenv/commit/ca95117)
    - Exclusion du fichier `package.lock` des mises à jour automatiques de dependabot. [#22391f0](https://github.com/MTES-MCT/monitorenv/commit/22391f0)
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité. [#88cfd23](https://github.com/MTES-MCT/monitorenv/commit/88cfd23)
    - Correction de plusieurs erreurs de type. [#36dfa21](https://github.com/MTES-MCT/monitorenv/commit/36dfa21)
    - Corrections et optimisations liées à la gestion des données de position des navires (AIS). [#df2d9b2](https://github.com/MTES-MCT/monitorenv/commit/df2d9b2) et suivantes.
    - Renommage de `sent_at` et refactoring utilisant le timestamp PK. [#e09f81e](https://github.com/MTES-MCT/monitorenv/commit/e09f81e)

### Autres changements

- Suppression de secrets inutiles. [#6ec036f](https://github.com/MTES-MCT/monitorenv/commit/6ec036f)
- Ajout d'un message d'avertissement pour les tags en cours de complétion. [#d68436c](https://github.com/MTES-MCT/monitorenv/commit/d68436c)
- Correction de tests unitaires. [#bf3541b](https://github.com/MTES-MCT/monitorenv/commit/bf3541b)
- Amélioration de la visibilité de l'environnement (intégration/pré-production) et suppression du feature flag "Regulatory areas". [#23a0420](https://github.com/MTES-MCT/monitorenv/commit/23a0420)
- Correction de l'URL de la favicon. [#24ee410](https://github.com/MTES-MCT/monitorenv/commit/24ee410)
- Ajout d'un titre aux options du sélecteur Natinf. [#096ccb4](https://github.com/MTES-MCT/monitorenv/commit/096ccb4)
