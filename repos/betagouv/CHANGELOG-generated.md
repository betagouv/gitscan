# Synthèse d'activité : betagouv (du 24/06 au 24/07)

## Résumé de l'activité
L'activité récente de l'organisation betagouv a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et améliorer la stabilité. Des efforts significatifs ont été déployés pour moderniser l'infrastructure de certains projets (passage à Poetry, refonte des migrations), et pour enrichir les données disponibles (ajout d'informations sur les médicaments, synchronisation avec des sources externes). Plusieurs projets ont également vu des améliorations de l'interface utilisateur et des fonctionnalités, comme l'ajout de nouvelles options de recherche, la simplification des formulaires et l'amélioration de la gestion des données. Les projets `sylvasan`, `transports-sanitaires`, `zacharie` et `mon-aide-cyber` ont été particulièrement actifs.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité :
- Correction d'une vulnérabilité XSS dans [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice).
- Mise à jour de dépendances vulnérables dans [mes-aides-analytics](/repos/betagouv/mes-aides-analytics).
- Renforcement de la sécurité des communications avec TLS et authentification par certificat dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).
- Ajout d'une vérification du certificat MQC dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).
- Intégration de `checkov` et `zizmor` pour la validation de la configuration dans [lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit).

## Autres changements notables
- Refonte des migrations de données dans [infomedicament](/repos/betagouv/infomedicament).
- Passage à Poetry pour la gestion des dépendances dans [infomedicament_data](/repos/betagouv/infomedicament_data).
- Refonte de l'architecture et des tests dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).
- Refactorisation de l'API et ajout d'un module de consommateurs dans [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- Migration vers pnpm dans [sante-mentale-etudiant](/repos/betagouv/sante-mentale-etudiant).
- Refonte de l'interface utilisateur et des tests dans [maestro](/repos/betagouv/maestro).

## Dépôts les plus actifs
- [zacharie](/repos/betagouv/zacharie) : Amélioration du tableau de bord SVI, simplification de l'acceptation SVI, refonte des statistiques et ajout d'une interface pour les laboratoires.
- [sylvasan](/repos/betagouv/sylvasan) : Ajout de nouvelles fonctionnalités (duplication d'enquêtes, gestion des follow-ups, suppression de réponses) et améliorations de la sécurité.
- [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Refonte majeure de l'application, fusion de l'identification et du simulateur, ajout de nouvelles fonctionnalités et amélioration de l'architecture.
- [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) : Amélioration de la sécurité, ajout de nouvelles fonctionnalités et corrections de bugs.
- [jeveuxaider-back](/repos/betagouv/jeveuxaider-back) : Amélioration de la synchronisation avec Airtable, gestion des missions et corrections de bugs.
