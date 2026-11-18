## Changelog : transport-sanitaire (30 derniers jours, au 17 novembre 2026)

### Résumé
Le projet a franchi une étape majeure avec le passage en version 1.2.0. Les évolutions récentes se sont concentrées sur l'intégration des nouvelles règles métier (contrat v10.2.2), l'amélioration de la génération et de la mise en page des documents PDF (fiches patient), ainsi que sur un renforcement massif de la traçabilité des parcours utilisateurs pour permettre une analyse plus fine des simulations.

### Évolutions fonctionnelles
- **Intégration du contrat v10.2.2** : Mise à jour complète des règles métier, de la validation des règles croisées et de la gestion des événements selon la dernière version du contrat [#497, #504, #506, #507].
- **Amélioration de la génération documentaire** : Optimisation de la création des documents PDF (DAP, PMT et R3), incluant une gestion automatique de la taille du texte pour qu'il s'adapte aux cadres des formulaires et la possibilité de télécharger les fiches patient [#129, #130, #157, #158, #159, #211, #212, #214, #228, #229, #230, #231, #234].
- **Affinement de la simulation** : 
    - Meilleure gestion des trajets (parties terrestres) et de l'urgence [#354, #362, #365, #366, #479, #480].
    - Détection et signalement des incohérences de saisie ou des dates invalides [#411, #435, #437, #439].
    - Nouveaux scénarios de simulation pour tester les blocages spécifiques du parcours [#466, #478, #486].
- **Expérience utilisateur** : 
    - Amélioration de l'interface avec des cases à cocher présentées sous forme de cartes et un stepper de parcours plus clair [#187, #210, #219, #224].
    - Ajout d'une invitation à donner un avis à l'utilisateur après l'affichage du résultat [#195, #237].

### Évolutions techniques
- **Refonte architecturale (DDD)** : Transition vers une architecture orientée domaine (*Domain Driven Design*) avec l'utilisation de *Value Objects* et de *Factories* pour la gestion des questions et des faits [#463, #446, #456, #216].
- **Observabilité et traçabilité** : Mise en place d'un système de journalisation (journal des parcours) extrêmement détaillé, permettant de suivre les clics, la taille des champs, les boutons exposés et les versions des documents pour faciliter le débogage et l'analyse de données [#382, #383, #384, #385, #386, #387, #388, #389, #412, #415, #416, #424, #426, #430, #433, #434, #436, #438, #491, #497, #506, #508, #509].
- **Qualité et Tests** : 
    - Introduction de tests de bout en bout dans un véritable navigateur avec Playwright [#461].
    - Stabilisation et accélération de la suite de tests existante [#457, #458].
- **Sécurité et CI/CD** : 
    - Protection de l'API contre les abus [#451, #454].
    - Déploiement de la CI sur l'environnement de staging et mise en place de règles de protection des branches [#460].

### Autres changements
- **Documentation** : Rédaction de documents de décision d'architecture (ADR), mise à jour du glossaire métier et documentation des compétences du projet [#91, #151, #238, #239, #252, #264, #268, #393, #463].
- **Maintenance** : Renommage officiel du dépôt en `transport-sanitaire` [#217].
