# Synthèse d'activité : betagouv (du 01/07 au 15/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique de modernisation des outils et une amélioration de l'expérience utilisateur. On note des avancées majeures dans la simplification des parcours (nouveaux simulateurs pour les frontaliers dans [mon-entreprise](/repos/betagouv/mon-entreprise), gestion des rendez-vous dans [rdv-service-public](/repos/betagouv/rdv-service-public)) et une montée en puissance de l'automatisation des processus métiers, notamment pour le suivi des données de santé et de laboratoire ([maestro](/repos/betagouv/maestro)).

L'intégration de l'intelligence artificielle pour la création de contenus pédagogiques ([science-infuse](/repos/betagouv/science-infuse)) et le renforcement de la qualité logicielle via de nouvelles architectures et des outils de design system ([standards](/repos/betagouv/standards), [lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit)) démontrent une volonté d'accroître la valeur ajoutée et la fiabilité des services mis à disposition des citoyens et des agents.

## Sécurité
- **Renforcement des communications et de l'authentification** : Implémentation du chiffrement TLS et de l'authentification par certificat pour [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus) et vérification des certificats MQC dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).
- **Correction de vulnérabilités** : Résolution de failles critiques, notamment sur la gestion des sessions dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) et des vulnérabilités XSS ou d'authentification dans [nitrates](/repos/betagouv/nitrates).
- **Protection des infrastructures** : Activation de pare-feu applicatifs (WAF) pour [pass-sport](/repos/betagouv/pass-sport) et intégration d'outils d'analyse de configuration (zizmor, checkov) pour sécuriser les pipelines CI/CD dans [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) et [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- **Remédiation des dépendances** : Correction de vulnérabilités de haute sévérité sur les dépendances dans [reva](/repos/betagouv/reva) et [mon-profil-anssi](/repos/betagouv/mon-profil-anssi).

## Autres changements notables
- **Modernisation technologique et architecturale** : Passage à Rails 8 et Ruby 3.4 pour [rdv-service-public](/repos/betagouv/rdv-service-public), publication de la version 2.0 des [standards](/repos/betagouv/standards), et refonte profonde du moteur d'autorisation de l'API dans [reva](/repos/betagouv/reva).
- **Refonte des simulateurs et de l'expérience usager** : Restructuration majeure de l'architecture des simulateurs dans [mon-entreprise](/repos/betagouv/mon-entreprise) et fusion de l'application d'identification et du simulateur dans [transports-sanitaires](/repos/betagouv/transports-sanitaires).
- **Automatisation et IA** : Développement de fonctionnalités de génération de contenu par IA dans [science-infuse](/repos/betagouv/science-infuse) et automatisation de la lecture de rapports PDF pour [maestro](/repos/betagouv/maestro).
- **Évolutions infrastructurelles** : Initialisation de l'infrastructure en tant que code (IaC) pour [nitrates-iac](/repos/betagouv/nitrates-iac) et adoption de Nix pour [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).

## Dépôts les plus actifs
- [zacharie](/repos/betagouv/zacharie) : Amélioration du suivi SVI et de l'expérience des collecteurs.
- [sylvasan](/repos/betagouv/sylvasan) : Optimisation de la précision géographique et de la saisie mobile.
- [rdv-service-public](/repos/betagouv/rdv-service-public) : Modernisation de l'infrastructure et intégration du DSFR.
- [reva](/repos/betagouv/reva) : Évolutions du parcours candidat et refonte de la sécurité API.
- [nitrates](/repos/betagouv/nitrates) : Refonte des formulaires et renforcement de la sécurité.
- [mon-entreprise](/repos/betagouv/mon-entreprise) : Lancement de nouveaux simulateurs et refonte architecturale.
- [maestro](/repos/betagouv/maestro) : Automatisation des échanges avec les laboratoires et gestion des utilisateurs.
- [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant) : Structuration du contenu et nouveaux modules d'aide.
