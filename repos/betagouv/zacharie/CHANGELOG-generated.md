## Changelog : zacharie (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur autour de la gestion des carcasses et des fiches, ainsi que sur la correction de plusieurs bugs et l'optimisation de la plateforme. Des améliorations significatives ont été apportées à l'interface utilisateur, notamment pour les chasseurs, et des fonctionnalités ont été ajoutées pour faciliter la gestion des examens initiaux et des bracelets.

### Évolutions fonctionnelles
- **Gestion des carcasses :**
    - Ajout d'une page dédiée aux carcasses avec une interface améliorée [#353](https://github.com/betagouv/zacharie/issues/353).
    - Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial [#383](https://github.com/betagouv/zacharie/issues/383).
    - Amélioration de l'affichage des commentaires des intermédiaires dans la modale des fiches [#358](https://github.com/betagouv/zacharie/issues/358).
    - Chargement des données par carcasses plutôt que par fiches pour une meilleure performance [#392](https://github.com/betagouv/zacharie/issues/392).
- **Interface utilisateur :**
    - Amélioration du style du tableau de bord chasseur [#401](https://github.com/betagouv/zacharie/issues/401).
    - Adaptation de la responsivité du formulaire d'adresse [#403](https://github.com/betagouv/zacharie/issues/403).
    - Ajout d'une page 404 personnalisée [#394](https://github.com/betagouv/zacharie/issues/394).
    - Amélioration de l'UI/UX pour la gestion des carcasses [#373](https://github.com/betagouv/zacharie/issues/373).
    - Uniformisation de l'interface pour la création d'associations de chasse [#380](https://github.com/betagouv/zacharie/issues/380).
- **Autres améliorations :**
    - Ajout d'un quiz pour le prélèvement et l'assiette [#361](https://github.com/betagouv/zacharie/issues/361).
    - Ajout d'une liste de lésions [#331](https://github.com/betagouv/zacharie/issues/331).
    - Ajout de scripts de démo pour simuler l'activité ETG [#388](https://github.com/betagouv/zacharie/issues/388).
    - Correction du wording pour les carcasses et les lots [#398](https://github.com/betagouv/zacharie/issues/398).

### Évolutions techniques
- **Refactoring et nettoyage du code :**
    - Nettoyage du code mort relatif à l'ancien tableau de bord partagé [#391](https://github.com/betagouv/zacharie/issues/391).
    - Simplification des contrôleurs utilisateurs [#364](https://github.com/betagouv/zacharie/issues/364).
    - Suppression de code legacy [#368](https://github.com/betagouv/zacharie/issues/368).
    - Split des contrôleurs admin [#369](https://github.com/betagouv/zacharie/issues/369).
    - Nettoyage des fonctions de synchronisation [#371](https://github.com/betagouv/zacharie/issues/371).
- **Tests :**
    - Ajout de tests de non-régression pour préparer le renversement du GET fei vers GET carcasses [#384](https://github.com/betagouv/zacharie/issues/384).
    - Ajout de nouveaux tests [#340](https://github.com/betagouv/zacharie/issues/340).
    - Correction de tests flaky [#352](https://github.com/betagouv/zacharie/issues/352).
- **Infrastructure et CI/CD :**
    - Ajout de Prettier dans le workflow CI/CD [#393](https://github.com/betagouv/zacharie/issues/393).
    - Mise en place d'un serveur statique pour les tests [#334](https://github.com/betagouv/zacharie/issues/334).
- **Expo :**
    - Intégration du support offline avec Expo [#327](https://github.com/betagouv/zacharie/issues/327).
    - Correction de problèmes liés à l'URL initiale d'Expo [#337](https://github.com/betagouv/zacharie/issues/337).
    - Ajout d'un bearer token pour les appels API dans Expo [#336](https://github.com/betagouv/zacharie/issues/336).

### Autres changements
- Correction du reset du store à la déconnexion [#385](https://github.com/betagouv/zacharie/issues/385).
- Correction du timeout pour le clear cache [#379](https://github.com/betagouv/zacharie/issues/379).
- Correction de l'accès aux destinataires des fiches pour les chasseurs [#378](https://github.com/betagouv/zacharie/issues/378).
- Suppression du bouton de création de fiche pour les simples chasseurs [#375](https://github.com/betagouv/zacharie/issues/375).
- Suppression des anciens liens du backend [#372](https://github.com/betagouv/zacharie/issues/372).
- Suppression de l'invitation pour les chasseurs [#377](https://github.com/betagouv/zacharie/issues/377).
- Correction du toggle admin [#376](https://github.com/betagouv/zacharie/issues/376).
- Correction du calcul BPH [#326](https://github.com/betagouv/zacharie/issues/326).
- Correction de l'activation/désactivation SVI [#335](https://github.com/betagouv/zacharie/issues/335).
- Optimisation des appels et gestion des filtres [#390](https://github.com/betagouv/zacharie/issues/390).
- Correction de bugs divers et amélioration de la stabilité de la plateforme.
