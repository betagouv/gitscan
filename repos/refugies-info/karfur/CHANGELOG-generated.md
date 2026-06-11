## Changelog : karfur (30 derniers jours, au 10 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment sur les fiches RCO (Référentiel Commun d'Offres) pour mobile, et corrige des bugs liés à l'affichage et à la connexion. Des efforts ont également été déployés pour améliorer la gestion des connaissances des agents, avec l'ajout de nouvelles fonctionnalités pour l'indexation et l'export des données, ainsi que des corrections de sécurité et de performance.

### Évolutions fonctionnelles
- Correction de bugs d'affichage sur les fiches RCO sur les plateformes Android et iOS [#3792](https://github.com/refugies-info/karfur/pull/3792).
- Correction d'un bug empêchant la prévisualisation des fiches [#3798](https://github.com/refugies-info/karfur/pull/3798).
- Correction d'un problème de connexion et de réinitialisation de mot de passe [#3789](https://github.com/refugies-info/karfur/pull/3789).
- Ajout du skill QMD officiel [#3800](https://github.com/refugies-info/karfur/pull/3800) et définition du contrat QMD pour les tests de skills et le corpus [#3797](https://github.com/refugies-info/karfur/pull/3797).
- Amélioration de l'affichage de l'adresse postale sur les fiches RCO [#3778](https://github.com/refugies-info/karfur/pull/3778).
- Correction de l'affichage des accents dans le moteur de recherche [#3769](https://github.com/refugies-info/karfur/pull/3769).
- Mise à jour des mentions légales sur le site et l'application [#3785](https://github.com/refugies-info/karfur/pull/3785).
- Suppression du label "IA" sur les fiches RCO [#3784](https://github.com/refugies-info/karfur/pull/3784).

### Évolutions techniques
- Fiabilisation de la normalisation Unicode des chemins exportés.
- Amélioration de la gestion des doublons pour l'agent, avec ajout d'un endpoint de détection [#3754](https://github.com/refugies-info/karfur/pull/3754).
- Correction de la gestion des valeurs nulles pour le prénom lors de l'authentification SSO [#3751](https://github.com/refugies-info/karfur/pull/3751).
- Mise à jour de la version d'Expo GitHub Action.
- Amélioration de la structure et de la documentation du corpus documentaire agent.
- Correction de problèmes liés aux tests Jest sur mobile.
- Ajout de GitLeaks pour la détection de secrets dans le code.
- Mise à jour des dépendances et correction de vulnérabilités de sécurité.

### Autres changements
- Documentation : mise à jour de la référence MCP QMD [#3800](https://github.com/refugies-info/karfur/pull/3800).
- Nettoyage et normalisation des noms de fichiers exportés du corpus agent.
- Suppression de code dupliqué.
- Amélioration des messages de log.
- Correction de problèmes de responsive design sur les pages de login et d'accueil.
- Suppression du badge RCO et des styles associés.
- Correction de problèmes liés à l'affichage des champs d'adresse.
- Amélioration de la gestion des erreurs et des valeurs nulles.
