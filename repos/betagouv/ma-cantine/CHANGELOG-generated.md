## Changelog : ma-cantine (30 derniers jours, au 11 novembre 2026)

### Résumé
Ce mois-ci a été marqué par une préparation intensive de la campagne de télédéclaration 2026, avec l'introduction de nouveaux volets thématiques (gaspillage, menu végétarien, substitution plastique) et une refonte de l'interface pour faciliter la saisie. Parallèlement, une expérimentation sur les "Petites Structures" a été lancée pour simplifier certains processus, et le système de traçabilité (EventLog) a été considérablement renforcé pour améliorer la sécurité et l'audit des données.

### Évolutions fonctionnelles
- **Télédéclaration & Diagnostics :**
    - Ajout de nouveaux volets thématiques : Gaspillage, Substitution plastique, Information convives et Menu végétarien ([#7537](https://github.com/betagouv/ma-cantine/issues/7537), [#7531](https://github.com/betagouv/ma-cantine/issues/7531), [#7527](https://github.com/betagouv/ma-cantine/issues/7527), [#7473](https://github.com/betagouv/ma-cantine/issues/7473)).
    - Amélioration de l'expérience utilisateur : icônes de progression dynamiques, affichage des erreurs en temps réel et résumé du bilan dynamisé ([#7545](https://github.com/betagouv/ma-cantine/issues/7545), [#7548](https://github.com/betagouv/ma-cantine/issues/7548), [#7570](https://github.com/betagouv/ma-cantine/issues/7570)).
    - Calcul des badges de complétion par année pour les volets thématiques ([#7579](https://github.com/betagouv/ma-cantine/issues/7579)).
    - Mise à jour des formulaires et des champs pour la campagne 2026 ([#7520](https://github.com/betagouv/ma-cantine/issues/7520), [#7521](https://github.com/betagouv/ma-cantine/issues/7521)).
- **Petites Structures :**
    - Lancement de l'expérimentation "Petites structures" : nouveau champ de classification permettant d'alléger certaines saisies (ex: famille de produits facultative) ([#7584](https://github.com/betagouv/ma-cantine/issues/7584), [#7593](https://github.com/betagouv/ma-cantine/issues/7593)).
- **Imports :**
    - Mise à jour des schémas d'importation pour le format 2026 ([#7469](https://github.com/betagouv/ma-cantine/issues/7469), [#7467](https://github.com/betagouv/ma-cantine/issues/7467)).
    - Nouvelle possibilité d'importation par identifiant (ID) pour les bilans détaillés ([#7494](https://github.com/betagouv/ma-cantine/issues/7494), [#7493](https://github.com/betagouv/ma-cantine/issues/7493)).
- **Interface & Navigation :**
    - Réorganisation du menu principal pour valoriser l'outil de suivi anti-gaspi ([#7367](https://github.com/betagouv/ma-cantine/issues/7367)).
    - Amélioration de la visibilité des informations sur la page établissement ([#7522](https://github.com/betagouv/ma-cantine/issues/7522)).

### Évolutions techniques
- **Architecture & Modèles :**
    - Refonte majeure du modèle `Diagnostics` via l'utilisation de mixins pour une meilleure organisation des champs par volet ([#7442](https://github.com/betagouv/ma-cantine/issues/7442), [#7443](https://github.com/betagouv/ma-cantine/issues/7443), [#7444](https://github.com/betagouv/ma-cantine/issues/7444)).
    - Création d'une application dédiée `imports` pour centraliser la logique d'importation ([#7450](https://github.com/betagouv/ma-cantine/issues/7450)).
    - Mise en place d'un système d'audit complet (`EventLog`) pour tracer les appels API, les imports et les tâches asynchrones ([#7311](https://github.com/betagouv/ma-cantine/issues/7311), [#7321](https://github.com/betagouv/ma-cantine/issues/7321), [#7421](https://github.com/betagouv/ma-cantine/issues/7421)).
- **API :**
    - Ouverture de l'API v2 (bilans et volets) aux éditeurs via OAuth2 ([#7577](https://github.com/betagouv/ma-cantine/issues/7577)).
    - Amélioration de l'API pour retourner des informations détaillées par volet (état de remplissage, propreté) ([#7532](https://github.com/betagouv/ma-cantine/issues/7532), [#7533](https://github.com/betagouv/ma-cantine/issues/7533), [#7534](https://github.com/betagouv/ma-cantine/issues/7534), [#7536](https://github.com/betagouv/ma-cantine/issues/7536)).
- **Sécurité :**
    - Correction de plusieurs vulnérabilités de type XSS (Stored-XSS) sur les formulaires et l'administration ([#7398](https://github.com/betagouv/ma-cantine/issues/7398), [#7397](https://github.com/betagouv/ma-cantine/issues/7397), [#7396](https://github.com/betagouv/ma-cantine/issues/7396)).
    - Renforcement de la sécurité lors de l'authentification (prévention de l'énumération d'emails et correction de contournement) ([#7395](https://github.com/betagouv/ma-cantine/issues/7395), [#7393](https://github.com/betagouv/ma-cantine/issues/7393)).
- **Infrastructure & CI/CD :**
    - Optimisation des pipelines CI avec des timeouts plus courts ([#7429](https://github.com/betagouv/ma-cantine/issues/7429)).
    - Mise à jour de la version de Python pour les jobs dbt ([#7404](https://github.com/betagouv/ma-cantine/issues/7404)).

### Autres changements
- Mise à jour de la documentation de l'API ([#7302](https://github.com/betagouv/ma-cantine/issues/7302)).
- Ajout d'un fichier `SECURITY.md` ([#7413](https://github.com/betagouv/ma-cantine/issues/7413)).
- Nettoyage de code et refactorisation de diverses commandes asynchrones ([#7415](https://github.com/betagouv/ma-cantine/issues/7415), [#7416](https://github.com/betagouv/ma-cantine/issues/7416), [#7417](https://github.com/betagouv/ma-cantine/issues/7417), [#7418](https://github.com/betagouv/ma-cantine/issues/7418), [#7419](https://github.com/betagouv/ma-cantine/issues/7419)).
