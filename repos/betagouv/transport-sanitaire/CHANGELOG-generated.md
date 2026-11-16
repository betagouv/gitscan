## Changelog : transport-sanitaire (30 derniers jours, au 13 novembre 2026)

### Résumé
Cette période est marquée par le passage majeur à la version 1.0.0 du simulateur. Les évolutions se sont concentrées sur la fiabilisation de l'expérience utilisateur (meilleure gestion des formulaires et génération de documents PDF) et sur un effort massif de traçabilité pour permettre un suivi précis des parcours utilisateurs.

### Évolutions fonctionnelles
- **Génération de documents** : possibilité de consulter l'aperçu, d'imprimer et de télécharger les fiches patients en format PDF ([#234](https://github.com/betagouv/transport-sanitaire/issues/234), [#211](https://github.com/betagouv/transport-sanitaire/issues/211)).
- **Améliorations de l'interface** :
    - Présentation des choix sous forme de cartes pour une meilleure lisibilité ([#210](https://github.com/betagouv/transport-sanitaire/issues/210)).
    - Ajout de titres de sections dans le parcours et ajustement automatique de la taille du texte pour l'affichage ([#224](https://github.com/betagouv/transport-sanitaire/issues/224), [#232](https://github.com/betagouv/transport-sanitaire/issues/232)).
    - Invitation à donner un avis après l'obtention du résultat ([#237](https://github.com/betagouv/transport-sanitaire/issues/237)).
- **Nouvelles règles de saisie** : intégration de questions spécifiques sur l'urgence, les champs médicaux multilignes et le sens du trajet ([#362](https://github.com/betagouv/transport-sanitaire/issues/362), [#364](https://github.com/betagouv/transport-sanitaire/issues/364), [#366](https://github.com/betagouv/transport-sanitaire/issues/366)).
- **Corrections de cohérence** :
    - Effacement automatique des réponses devenues obsolètes lorsque l'utilisateur change de catégorie ou de question ([#449](https://github.com/betagouv/transport-sanitaire/issues/449), [#444](https://github.com/betagouv/transport-sanitaire/issues/444), [#431](https://github.com/betagouv/transport-sanitaire/issues/431), [#429](https://github.com/betagouv/transport-sanitaire/issues/429)).
    - Détection et signalement des dates invalides ou futures ([#442](https://github.com/betagouv/transport-sanitaire/issues/442), [#439](https://github.com/betagouv/transport-sanitaire/issues/439)).
    - Alertes en cas d'incohérence lors de la navigation ([#435](https://github.com/betagouv/transport-sanitaire/issues/435), [#437](https://github.com/betagouv/transport-sanitaire/issues/437)).

### Évolutions techniques
- **Observabilité et suivi** : mise en place d'un journal de bord détaillé pour suivre les parcours utilisateurs (chargement de pages, clics sur les boutons, versions des documents affichés et taille des champs) ([#438](https://github.com/betagouv/transport-sanitaire/issues/438), [#436](https://github.com/betagouv/transport-sanitaire/issues/436), [#430](https://github.com/betagouv/transport-sanitaire/issues/430), [#426](https://github.com/betagouv/transport-sanitaire/issues/426), [#424](https://github.com/betagouv/transport-sanitaire/issues/424), [#415](https://github.com/betagouv/transport-sanitaire/issues/415), [#412](https://github.com/betagouv/transport-sanitaire/issues/412), [#409](https://github.com/betagouv/transport-sanitaire/issues/409)).
- **Architecture et Refactoring** :
    - Restructuration du moteur de règles pour séparer la logique métier du socle technique ([#216](https://github.com/betagouv/transport-sanitaire/issues/216), [#250](https://github.com/betagouv/transport-sanitaire/issues/250), [#249](https://github.com/betagouv/transport-sanitaire/issues/249)).
    - Optimisation de la lecture des abstractions dans l'arbre de décision ([#337](https://github.com/betagouv/transport-sanitaire/issues/337)).
- **Tests** : augmentation significative de la couverture de tests sur les scénarios de recette (N2, N4) et la génération de documents ([#313](https://github.com/betagouv/transport-sanitaire/issues/313), [#314](https://github.com/betagouv/transport-sanitaire/issues/314), [#293](https://github.com/betagouv/transport-sanitaire/issues/293), [#291](https://github.com/betagouv/transport-sanitaire/issues/291), [#270](https://github.com/betagouv/transport-sanitaire/issues/270), [#310](https://github.com/betagouv/transport-sanitaire/issues/310)).
- **Mises à jour métier** : intégration successive des modèles de règles métier v10.1.4 jusqu'à la v10.1.8.

### Autres changements
- **Documentation** : mise à jour du glossaire et documentation des processus de décision ([#238](https://github.com/betagouv/transport-sanitaire/issues/238), [#252](https://github.com/betagouv/transport-sanitaire/issues/252)).
- **Maintenance** : renommage officiel du dépôt en `transport-sanitaire` ([#217](https://github.com/betagouv/transport-sanitaire/issues/217)).
