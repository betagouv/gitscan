## Changelog : messages (30 derniers jours, au 23 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via l'ajout de bannières d'information (réponses automatiques, messages de service) et une optimisation de l'interface mobile. La sécurité a été renforcée par un durcissement des accès et une mise à jour des certificats de confiance, tandis que l'infrastructure a bénéficié de montées de version critiques (Python, Keycloak).

### Évolutions fonctionnelles
- **Interface et expérience utilisateur**
    - Ajout de bannières visuelles pour signaler l'activation d'une réponse automatique ou l'affichage d'un message de service.
    - Introduction d'une confirmation avant la suppression de brouillons [#817](https://github.com/suitenumerique/messages/issues/817).
    - Amélioration de la gestion des messages MBOX (mots-clés et support de format).
    - Corrections diverses de l'interface : badges de messages non lus sur le favicon, menus déroulants [#808](https://github.com/suitenumerique/messages/issues/808), et popovers de recherche ou de suggestion d'utilisateurs.
    - Correction des traductions en néerlandais.
    - Masquage de la clé API dans le modal d'intégration pour plus de sécurité.
- **Expérience Mobile**
    - Optimisation de l'affichage en mode paysage pour la composition de messages.
    - Résolution de problèmes de focus du clavier et de l'éditeur sur les appareils tactiles.
    - Corrections de plusieurs problèmes de style visuel.

### Évolutions techniques
- **Sécurité et Infrastructure**
    - Renforcement du contrôle des accès (scoping) et des requêtes sortantes.
    - Suspension des clés API personnelles lors de certaines opérations de cascade [#804](https://github.com/suitenumerique/messages/issues/804).
    - Utilisation de `SecretFileValue` pour sécuriser les paramètres sensibles.
    - Mise à jour des composants critiques : Python 3.14.8 [#821](https://github.com/suitenumerique/messages/issues/821), Keycloak 26.8.1 [#813](https://github.com/suitenumerique/messages/issues/813) et Caddy 2.11.7.
    - Rafraîchissement des images de base et des certificats CA [#829](https://github.com/suitenumerique/messages/issues/829), incluant le retrait du certificat racine emSign ECC compromis.
- **Backend et Performance**
    - Mise en place de la pagination pour la vue des métriques d'utilisation [#832](https://github.com/suitenumerique/messages/issues/832).
    - Déplacement des tâches d'exportation vers le worker d'importation [#805](https://github.com/suitenumerique/messages/issues/805).
    - Correction de la recherche de threads en l'absence de configuration OpenSearch.
- **Frontend et Mobile**
    - Mise à jour de Capacitor vers la version 8.5 avec adoption du cycle de vie UIScene.
    - Mise à jour du kit d'interface utilisateur (ui-kit) vers la version 1.3.0.
    - Optimisation du frontend pour éviter les doubles initialisations de la bibliothèque Lagaufre [#823](https://github.com/suitenumerique/messages/issues/823).
    - Amélioration de la compatibilité des images Docker avec Podman [#820](https://github.com/suitenumerique/messages/issues/820).
- **Tests**
    - Ajout de tests de bout en bout (E2E) pour le thème Keycloak `lst-dsfr`.

### Autres changements
- Ajout d'un Dockerfile et d'un modèle de menace pour l'enrôlement du scanner OSS.
