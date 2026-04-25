## Changelog : monitorenv (30 derniers jours, au 14 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur et aux fonctionnalités de gestion des zones de vigilance et des zones réglementaires. Des optimisations ont également été apportées au traitement des données de navires et à la sécurité de l'application.

### Évolutions fonctionnelles
- **Zones de vigilance :**
    - Ajout d'un filtre pour afficher les zones de vigilance récentes [#405b92e](https://github.com/MTES-MCT/monitorenv/commit/405b92e).
    - Amélioration de l'affichage des zones de vigilance avec des lignes expansibles et un tri par date de création par défaut [#6430d0f](https://github.com/MTES-MCT/monitorenv/commit/6430d0f).
    - Ajout de colonnes épinglées pour une meilleure lisibilité [#207f6a8](https://github.com/MTES-MCT/monitorenv/commit/207f6a8).
    - Mise à jour des filtres pour les zones de vigilance [#3795f40](https://github.com/MTES-MCT/monitorenv/commit/3795f40).
- **Zones réglementaires :**
    - Corrections apportées au formulaire de création/modification des zones réglementaires [#6eaf503](https://github.com/MTES-MCT/monitorenv/commit/6eaf503).
    - Tri des zones réglementaires par front de mer [#c25727b](https://github.com/MTES-MCT/monitorenv/commit/c25727b).
    - Mise en évidence des zones réglementaires récentes ou mises à jour [#5bb0165](https://github.com/MTES-MCT/monitorenv/commit/5bb0165).
- **AMP (Autorisations de Mise en Place) :**
    - Mise en évidence des nouveaux AMP [#eed0ba0](https://github.com/MTES-MCT/monitorenv/commit/eed0ba0).
    - Correction du flux de données AMP [#dd1f770](https://github.com/MTES-MCT/monitorenv/commit/dd1f770).
- **Navires :**
    - Ajout du tonnage brut UMS aux informations du navire [#a3ed217](https://github.com/MTES-MCT/monitorenv/commit/a3ed217).
- **Interface utilisateur :**
    - Amélioration de la visibilité de l'environnement (intégration/pré-production) [#23a0420](https://github.com/MTES-MCT/monitorenv/commit/23a0420).
    - Correction de l'URL de la favicon [#24ee410](https://github.com/MTES-MCT/monitorenv/commit/24ee410).
    - Réajout de la bannière sur toutes les pages [#7ea7581](https://github.com/MTES-MCT/monitorenv/commit/7ea7581).
    - Mise en évidence des zones de vigilance et des zones réglementaires épinglées [#882d0bc](https://github.com/MTES-MCT/monitorenv/commit/882d0bc).

### Évolutions techniques
- **Base de données :**
    - Ajout d'un index sur les données d'identification [#eb8cb9d](https://github.com/MTES-MCT/monitorenv/commit/eb8cb9d).
    - Refactorisation du champ `sent_at` et utilisation du timestamp PK [#e09f81e](https://github.com/MTES-MCT/monitorenv/commit/e09f81e).
- **Sécurité :**
    - Vérification de la présence de la revendication `organizational_unit` pour renforcer la sécurité [#1608c9c](https://github.com/MTES-MCT/monitorenv/commit/1608c9c).
- **Traitement des données :**
    - Amélioration de la récupération des informations du navire par ID [#0860cc5](https://github.com/MTES-MCT/monitorenv/commit/0860cc5).
    - Correction de la source du timestamp pour le traitement des messages AIS [#df2d9b2](https://github.com/MTES-MCT/monitorenv/commit/df2d9b2).
    - Gestion des erreurs lors de la désérialisation des données [#b394679](https://github.com/MTES-MCT/monitorenv/commit/b394679).
- **CI/CD :**
    - Configuration d'un délai de 30 jours pour les mises à jour de dépendances via Dependabot [#ca95117](https://github.com/MTES-MCT/monitorenv/commit/ca95117).

### Autres changements
- Suppression de secrets inutiles [#6ec036f](https://github.com/MTES-MCT/monitorenv/commit/6ec036f).
- Correction des tests unitaires [#bf3541b](https://github.com/MTES-MCT/monitorenv/commit/bf3541b).
- Empêchement de la mise à jour des zones réglementaires dans la base de données CACEM sur le serveur d'intégration [#d753c0f](https://github.com/MTES-MCT/monitorenv/commit/d753c0f).
- Correction de l'affichage des calques et des axes dans le tableau de bord [#6aeff26](https://github.com/MTES-MCT/monitorenv/commit/6aeff26).
- Correction de l'affichage des zones réglementaires par axe dans le résumé [#268c4c1](https://github.com/MTES-MCT/monitorenv/commit/268c4c1).
- Ajout d'un titre aux options du sélecteur NatInf [#096ccb4](https://github.com/MTES-MCT/monitorenv/commit/096ccb4).
- Correction de l'ordre de vérification pour le contournement de l'email [#0a92d3e](https://github.com/MTES-MCT/monitorenv/commit/0a92d3e).
