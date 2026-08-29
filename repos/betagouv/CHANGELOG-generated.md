# Synthèse d'activité : betagouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de betagouv se concentre sur trois piliers majeurs : la modernisation des outils de santé et de suivi sanitaire ([seves](/repos/betagouv/seves), [sylvasan](/repos/betagouv/sylvasan), [zacharie](/repos/betagouv/zacharie)), l'amélioration de l'accompagnement des publics étudiants ([monlogementetudiant](/repos/betagouv/monlogementetudiant), [sante-psy](/repos/betagouv/sante-psy), [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant)), et le renforcement de la sécurité des infrastructures et des données ([lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit), [pass-sport](/repos/betagouv/pass-sport)).

Ces évolutions visent à offrir une meilleure précision des données (géolocalisation, calculs de taux), une expérience utilisateur plus fluide sur mobile et une fiabilité accrue des services grâce à des refontes architecturales et des automatisations de maintenance.

## Sécurité
- **Protection des accès et authentification** : Mise en place du MFA et de l'authentification ProConnect ([mon-service-securise](/repos/betagouv/mon-service-securise), [pitchou](/repos/betagouv/pitchou)), implémentation de l'authentification par certificat TLS ([lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus)) et activation de l'authentification à deux facteurs (2FA) pour les administrateurs ([recommandations-collaboratives](/repos/betagouv/recommandations-collaboratives)).
- **Correction de vulnérabilités** : Résolution de failles critiques liées à la gestion des sessions ([mon-suivi-justice](/repos/betagouv/mon-suivi-justice)), de vulnérabilités XSS ([nitrates](/repos/betagouv/nitrates)) et mise à jour de dépendances de sécurité ([mon-profil-anssi](/repos/betagouv/mon-profil-anssi), [lab-anssi-lib](/repos/betagouv/lab-anssi-lib)).
- **Sécurisation des infrastructures** : Activation d'un pare-feu applicatif (WAF) ([pass-sport](/repos/betagouv/pass-sport)), renforcement de la vérification des certificats pour les sauvegardes ([lab-anssi-admin](/repos/betagouv/lab-anssi-admin)) et intégration d'outils d'analyse de configuration dans les pipelines CI/CD ([mon-aide-cyber](/repos/betagouv/mon-aide-cyber), [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal)).

## Autres changements notables
- **Migrations et refontes architecturales** : Passage à Rails 8 ([rdv-service-public](/repos/betagouv/rdv-service-public)), refonte majeure du système de simulation ([mon-entreprise](/repos/betagouv/mon-entreprise)), et restructuration profonde du simulateur de transports ([transports-sanitaires](/repos/betagouv/transports-sanitaires)).
- **Évolutions des standards et outils de design** : Publication de la version 2.0 des standards ([standards](/repos/betagouv/standards)) et mise en conformité majeure des composants avec le DSFR ([lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit), [penpot-dsfr](/repos/betagouv/penpot-dsfr)).
- **Innovations et nouveaux services** : Lancement du connecteur Brevo-Sekoia ([sekoia-brevo-connector](/repos/betagouv/sekoia-brevo-connector)) et intégration de l'IA pour la génération de contenus pédagogiques ([science-infuse](/repos/betagouv/science-infuse)).

## Dépôts les plus actifs
- [sylvasan](/repos/betagouv/sylvasan) : Amélioration de la précision cartographique, de l'expérience de saisie terrain et de l'accessibilité.
- [monlogementetudiant](/repos/betagouv/monlogementetudiant) : Refonte de l'interface utilisateur (DSFR), fiabilisation du géocodage et automatisation de la gestion des données.
- [seves](/repos/betagouv/seves) : Optimisation de la gestion des alertes sanitaires, de la cartographie et de la saisie via les API SIRENE/BAN.
- [nitrates](/repos/betagouv/nitrates) : Refonte des formulaires pour le mobile, renforcement de la sécurité et mise en place d'une infrastructure GitOps.
- [lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit) : Mise en conformité DSFR des composants et migration vers Vite 8.
- [ma-cantine](/repos/betagouv/ma-cantine) : Refonte de l'espace établissement et enrichissement des indicateurs de diagnostic.
