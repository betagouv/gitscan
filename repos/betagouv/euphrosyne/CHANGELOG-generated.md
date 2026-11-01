## Changelog : euphrosyne (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement majeur de la sécurité et de la protection des données. Les mises à jour améliorent la protection des comptes utilisateurs, la gestion des sessions et la robustesse de l'application face aux vulnérabilités web, tout en consolidant la documentation technique.

### Évolutions fonctionnelles
- **Sécurité des comptes** :
    - Renforcement des exigences de complexité des mots de passe lors de la création de comptes [#2068](https://github.com/betagouv/euphrosyne/issues/2068).
    - Unification du mécanisme de verrouillage des comptes (après plusieurs tentatives infructueuses) entre l'interface web et les API [#2071](https://github.com/betagouv/euphrosyne/issues/2071).
- **Gestion des sessions** :
    - Mise en place de l'expiration automatique des sessions web en fonction du rôle de l'utilisateur [#2069](https://github.com/betagouv/euphrosyne/issues/2069).

### Évolutions techniques
- **Sécurité et protection des données** :
    - Correction de vulnérabilités de type XSS (Cross-Site Scripting) sur les pages de projets et dans les e-mails HTML.
    - Sécurisation des cookies de session et CSRF [#2073](https://github.com/betagouv/euphrosyne/issues/2073).
    - Renforcement de la validation des signatures des webhooks Tally [#2042](https://github.com/betagouv/euphrosyne/issues/2042).
    - Amélioration de la politique de sécurité du contenu (CSP) avec reporting des violations vers Sentry.
    - Sécurisation des segments d'URL des répertoires et restriction des origines de téléchargement lors des exports PDF.
    - Réduction de l'exposition des données personnelles dans les journaux de diagnostic et l'outil Sentry [#2067](https://github.com/betagouv/euphrosyne/issues/2067).
- **Maintenance et optimisation** :
    - Nettoyage du code par la suppression de fonctionnalités et de tests obsolètes (notamment l'export PDF des notebooks et certains rendus de groupes d'objets).
    - Mise en conformité de l'administration des logs d'e-mails avec Django 6.1.

### Autres changements
- **Documentation** :
    - Ajout de la documentation d'architecture technique (TAD).
    - Mise à jour de la documentation concernant l'emplacement des ressources Azure.
