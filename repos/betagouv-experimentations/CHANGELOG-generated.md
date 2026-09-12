# Synthèse d'activité : betagouv-experimentations (du 13/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est caractérisée par une phase intense de lancement de nouveaux prototypes visant à accélérer la création de services web pour l'administration. Ces projets s'appuient sur des technologies modernes (Next.js, PostgreSQL) et le Design System Français pour garantir une expérience utilisateur cohérente et rapide à déployer.

L'accent est mis sur l'automatisation des infrastructures via Coolify et l'intégration de l'intelligence artificielle pour assister les processus de développement. On note également l'émergence d'outils spécifiques, comme un CRM pour le suivi de contacts ou des outils de gestion de logs, démontrant une volonté de transformer ces expérimentations en solutions fonctionnelles.

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).

## Autres changements notables
- **Infrastructure et Déploiement** : Généralisation de l'usage de Coolify pour l'auto-provisionnement et la mise en place de workflows CI/CD sur l'ensemble des nouveaux projets ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [template-proto](/repos/betagouv-experimentations/template-proto)).
- **Intelligence Artificielle** : Intégration explicite des capacités de l'IA Claude dans les phases de build et de configuration des projets ([template-proto](/repos/betagouv-experimentations/template-proto), [repo-test](/repos/betagouv-experimentations/repo-test)).
- **Outils de monitoring** : Développement d'un proxy dédié à la récupération et à l'analyse des logs Coolify, incluant l'authentification via GitHub et la gestion de webhooks ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).
- **Automatisation technique** : Mise en place de l'automatisation des migrations de base de données au démarrage des conteneurs ([template-proto](/repos/betagouv-experimentations/template-proto)).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des contacts et des interactions pour l'équipe ASN.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un proxy pour la gestion robuste et l'authentification des logs de déploiement.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolution du template de prototypage avec ajout de tests de fumée et support IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application complète de gestion de tâches (CRUD) avec persistance de données.
