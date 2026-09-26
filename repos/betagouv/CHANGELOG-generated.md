# Synthèse d'activité : betagouv (du 01/03 au 30/09)

## Résumé de l'activité
L'activité de l'organisation a été marquée par le lancement de fonctionnalités majeures impactant directement les usagers et les professionnels. On note notamment l'enrichissement des capacités de gestion de la santé animale dans [seves](/repos/betagouv/seves), le déploiement des outils de gestion des VAE collectives dans [reva](/repos/betagouv/reva), et l'ouverture de nouveaux espaces dédiés aux étudiants dans [monlogementetudiant](/repos/betagouv/monlogementetudiant).

L'intégration de l'intelligence artificielle progresse de manière significative à travers des outils d'aide à la création de contenu pédagogique dans [science-infuse](/repos/betagouv/science-infuse), la mise à jour du moteur d'analyse dans [portail-rse-externe](/repos/betagouv/portail-rse-externe) et l'automatisation de la revue de code dans [mon-entreprise](/repos/betagouv/mon-entreprise). Parallèlement, une attention particulière a été portée à l'amélioration de l'expérience utilisateur (UX) et à la simplification des parcours métier, notamment via de nouveaux comparateurs de modèles dans [mon-entreprise](/repos/betagouv/mon-entreprise) et des interfaces de saisie terrain optimisées dans [sylvasan](/repos/betagouv/sylvasan).

## Sécurité
Une part importante des efforts a été consacrée au renforcement de la protection des données et à la correction de vulnérabilités critiques :
- **Protection des données et authentification** : Sécurisation massive des données personnelles (PII) et correction de failles (IDOR, injections) dans [service-national-universel](/repos/betagouv/service-national-universel), renforcement de l'authentification 2FA dans [reva](/repos/betagouv/reva) et [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes), et sécurisation des sessions dans [rdv-service-public](/repos/betagouv/rdv-service-public) et [mon-suivi-justice](/repos/betagouv/mon-suivi-justice).
- **Protection contre les attaques** : Mise en œuvre de politiques de sécurité strictes (CSP) et protection contre les injections dans [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) et [ma-cantine](/repos/betagouv/ma-cantine).
- **Automatisation de la sécurité** : Intégration de contrôles automatiques de vulnérabilités (CVE, Bandit) dans [transports-sanitaires-sites-conformes](/repos/betagouv/transports-sanitaires-sites-conformes) et de nouveaux outils d'analyse de configuration dans [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).

## Autres changements notables
- **Versions majeures et lancements** : Publication de la version 2.0 des [standards](/repos/betagouv/standards) et de la version 1.0.0 de [slack2tchap](/repos/betagouv/slack2tchap).
- **Refontes architecturales** : Restructuration profonde du simulateur dans [transports-sanitaires](/repos/betagouv/transports-sanitaires), modernisation de la stack technologique (PHP/Symfony) dans [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) et passage à une architecture "stateless" pour [slack2tchap](/repos/betagouv/slack2tchap).
- **Infrastructure et DevOps** : Initialisation de l'infrastructure en tant que code (IaC) pour [nitrates-iac](/repos/betagouv/nitrates-iac) et déploiement de nouveaux services sur Scalingo comme [scalingo-gotenberg](/repos/betagouv/scalingo-gotenberg).

## Dépôts les plus actifs
- [seves](/repos/betagouv/seves) : Développement majeur du module de Santé Animale et amélioration de la cartographie.
- [reva](/repos/betagouv/reva) : Gestion des VAE Collectives et refonte du système de droits d'accès.
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Création d'un comparateur de modèles et intégration de l'IA pour la revue de code.
- [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice) : Modernisation de la stack et amélioration de la gestion documentaire (PDF).
- [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Mise à jour des règles métier et refonte de l'architecture logicielle.
- [rdv-service-public](/repos/betagouv/rdv-service-public) : Lancement du système d'invitation usager et renforcement de la sécurité.
- [nitrates](/repos/betagouv/nitrates) : Amélioration de l'ergonomie DSFR et de l'observabilité de l'infrastructure.
