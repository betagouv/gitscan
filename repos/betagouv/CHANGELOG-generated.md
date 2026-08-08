# Synthèse d'activité : betagouv (du 01/07 au 06/08)

## Résumé de l'activité
L'activité de cette période est marquée par une modernisation profonde des outils de simulation et de suivi, ainsi que par l'intégration de nouvelles fonctionnalités innovantes. Des avancées majeures ont été réalisées pour simplifier les parcours usagers, notamment avec le lancement du simulateur pour les travailleurs frontaliers dans [mon-entreprise](/repos/betagouv/mon-entreprise) et l'ajout de fonctionnalités de génération de contenu pédagogique assistée par IA dans [science-infuse](/repos/betagouv/science-infuse).

Parallèlement, l'organisation a concentré ses efforts sur la fiabilité et la robustesse des services. Cela s'est traduit par des refontes architecturales importantes pour faciliter la maintenance à long terme, comme dans [reva](/repos/betagouv/reva) ou [transports-sanitaires](/repos/betagouv/transports-sanitaires), et par un renforcement systématique de la sécurité des données et des infrastructures.

## Sécurité
- **Protection des communications et authentification** : Implémentation du chiffrement TLS et de l'authentification par certificat dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus), mise en place de l'authentification à deux facteurs (2FA) pour les administrateurs de [recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives) et renforcement de la vérification des certificats dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).
- **Correction de vulnérabilités** : Résolution de failles critiques, notamment sur la gestion des sessions dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice), des vulnérabilités XSS dans [nitrates](/repos/betagouv/nitrates) et une correction de sécurité (CVE) dans [rdv-service-public](/repos/betagouv/rdv-service-public).
- **Protection des infrastructures** : Activation d'un pare-feu applicatif (WAF) pour protéger [pass-sport](/repos/betagouv/pass-sport) et intégration d'outils d'analyse de configuration (zizmor, checkov) pour sécuriser les pipelines CI/CD dans [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- **Contrôle des données** : Renforcement de la sécurité des profils dans [portail-rse](/repos/betagouv/portail-rse) et protection contre les injections dans [monlogementetudiant](/repos/betagouv/monlogementetudiant).

## Autres changements notables
- **Refontes architecturales** : Restructuration profonde des simulateurs dans [mon-entreprise](/repos/betagouv/mon-entreprise) pour séparer les données de la configuration, et migration vers un nouveau moteur de politiques pour une gestion granulaire des droits dans l'API de [reva](/repos/betagouv/reva).
- **Évolutions des standards et outils** : Publication de la version 2.0 des [standards](/repos/betagouv/standards) et modernisation de la génération de documents PDF via l'utilisation de Typst dans [mon-service-securise](/repos/betagouv/mon-service-securise).
- **Fusion et simplification de services** : Fusion de l'application d'identification et du simulateur dans [transports-sanitaires](/repos/betagouv/transports-sanitaires) pour unifier l'expérience utilisateur.
- **Optimisation des données** : Mise en place de la gestion de données "canoniques" pour garantir la qualité des programmes de transition écologique dans [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back).

## Dépôts les plus actifs
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Refonte majeure de l'architecture des simulateurs et lancement d'un nouveau service pour les frontaliers.
- [reva](/repos/betagouv/reva) : Évolutions importantes sur la gestion des droits d'accès et la sécurité de l'API.
- [nitrates](/repos/betagouv/nitrates) : Amélioration de l'expérience mobile, de la sécurité et de l'infrastructure CI/CD.
- [sylvasan](/repos/betagouv/sylvasan) : Introduction de la gestion des suivis et amélioration de la précision cartographique.
- [maestro](/repos/betagouv/maestro) : Enrichissement des outils de pilotage et fiabilisation des données de laboratoire.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Ajout de fonctionnalités de statistiques et de reporting pour les administrateurs.
- [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Refonte complète et fusion de l'application de simulation.
- [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant) : Développement de nouvelles fonctionnalités clés comme l'orientateur et la newsletter.
