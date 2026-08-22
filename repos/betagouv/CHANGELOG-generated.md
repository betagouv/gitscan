# Synthèse d'activité : betagouv (du 01/07 au 20/08)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une modernisation profonde des outils de pilotage et une automatisation accrue des processus métiers. Des avancées majeures ont été réalisées pour simplifier le travail des agents et des professionnels, notamment via l'automatisation des échanges avec les laboratoires dans [maestro](/repos/betagouv/maestro) et l'amélioration du suivi des dossiers dans [zacharie](/repos/betagouv/zacharie) ou [sante-psy](/repos/betagouv/sante-psy).

Parallèlement, l'expérience utilisateur a été enrichie par de nouveaux services de contenu et d'aide, comme les outils de création pédagogique assistée par IA dans [science-infuse](/repos/betagouv/science-infuse) ou la structuration de l'offre de santé mentale dans [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant). Ces évolutions visent à rendre les services plus intuitifs, plus accessibles et plus performants pour l'ensemble des usagers.

## Sécurité
- Correction d'une vulnérabilité critique sur la gestion des sessions utilisateurs dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice).
- Renforcement de la protection contre les attaques (XSS, authentification admin) dans [nitrates](/repos/betagouv/nitrates).
- Mise en place du chiffrement TLS et de l'authentification par certificat pour sécuriser les communications dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).
- Activation d'un pare-feu applicatif (WAF) pour protéger l'infrastructure de [pass-sport](/repos/betagouv/pass-sport).
- Intégration d'outils d'analyse automatique de la configuration pour prévenir les failles dans [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- Implémentation de l'authentification à deux facteurs (2FA) pour les administrateurs dans [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives).
- Vérification des certificats de sécurité pour les sauvegardes dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).

## Autres changements notables
- Publication de la version 2.0 des [standards](/repos/betagouv/standards).
- Refonte architecturale majeure fusionnant l'identification et le simulateur dans [transports-sanitaires](/repos/betagouv/transports-sanitaires).
- Modernisation des socles techniques, notamment le passage à Rails 8 pour [rdv-service-public](/repos/betagouv/rdv-service-public) et PHP 8.1 pour [maestro-wordpress](/repos/betagouv/maestro-wordpress).
- Automatisation des déploiements et mise en place de "Review Apps" pour tester les modifications en isolation dans [mon-entreprise](/repos/betagouv/mon-entreprise).
- Initialisation de l'infrastructure en tant que code (IaC) pour [nitrates-iac](/repos/betagouv/nitrates-iac).
- Optimisation de la gestion de la mémoire et des performances de recherche dans [ranking_methods](/repos/betagouv/ranking_methods) et [maestro](/repos/betagouv/maestro).

## Dépôts les plus actifs
- [maestro](/repos/betagouv/maestro) : Automatisation des échanges avec les laboratoires et gestion accrue de l'autonomie des coordinateurs.
- [sylvasan](/repos/betagouv/sylvasan) : Amélioration de la précision géographique, des exports de données et de l'ergonomie mobile.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Développement de nouveaux outils de reporting, de statistiques et de génération de documents PDF.
- [nitrates](/repos/betagouv/nitrates) : Refonte de l'expérience utilisateur sur mobile et renforcement global de la sécurité.
- [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Fusion de l'application d'identification et du simulateur avec une nouvelle architecture.
- [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant) : Structuration importante du contenu (articles, newsletter) et de l'interface utilisateur.
