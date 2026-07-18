# Synthèse d'activité : betagouv (du 23/06 au 23/07)

## Résumé de l'activité
L'organisation betagouv a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs projets. Un effort important a été consenti pour renforcer la sécurité, notamment avec des mises à jour de dépendances et l'implémentation de TLS. De nombreux projets ont bénéficié d'améliorations de l'expérience utilisateur, avec des refontes d'interfaces, l'ajout de nouvelles fonctionnalités et des corrections de bugs. L'intégration de données externes et l'automatisation de processus (synchronisation, CI/CD) ont également été des thèmes récurrents. Plusieurs projets ont progressé dans la préparation de nouvelles fonctionnalités, comme l'ajout de simulateurs et de systèmes d'alerte. Les projets `zacharie`, `transports-sanitaires`, `sante-psy`, `reva`, `mon-aide-cyber` et `infomedicament` ont été particulièrement actifs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction d'une vulnérabilité XSS dans [portail-rse](/repos/betagouv/portail-rse).
*   Mise à jour de la gem `rack-session` dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) pour corriger une vulnérabilité.
*   Implémentation de TLS et d'authentification par certificat dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).
*   Ajout d'une vérification du certificat MQC dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).
*   Correction d'une validation de date de naissance non sécurisée dans [jeveuxaider-front](/repos/betagouv/jeveuxaider-front).

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :

*   Refonte de l'architecture du simulateur de transport sanitaire dans [transports-sanitaires](/repos/betagouv/transports-sanitaires).
*   Migration vers pnpm dans [test-sme](/repos/betagouv/test-sme) et [oauth2-deploy-demo](/repos/betagouv/oauth2-deploy-demo).
*   Refactorisation de l'infrastructure CI/CD dans [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back).
*   Passage à Poetry pour la gestion des dépendances dans [infomedicament_data](/repos/betagouv/infomedicament_data).
*   Refactorisation du code et ajout de tests dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).

## Dépôts les plus actifs
*   [zacharie](/repos/betagouv/zacharie) : Ajout de nombreuses fonctionnalités pour améliorer la gestion des fiches et carcasses, notamment un tableau de bord SVI et une meilleure gestion des utilisateurs.
*   [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Refonte majeure de l'application avec fusion de l'identification et du simulateur, ajout de nouvelles fonctionnalités et amélioration de l'architecture.
*   [sante-psy](/repos/betagouv/sante-psy) : Amélioration de l'annuaire des psychologues, de la gestion des rendez-vous et de l'expérience utilisateur globale.
*   [reva](/repos/betagouv/reva) : Amélioration du parcours de dématérialisation autonome des VAE et renforcement de la sécurité.
*   [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) : Suppression de l'envoi en copie des demandes de devenir aidant et mise à jour des dépendances.
*   [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) et [jeveuxaider-back](/repos/betagouv/jeveuxaider-back) : Améliorations significatives des formulaires, de la gestion des missions et de la synchronisation avec Airtable.
*   [infomedicament](/repos/betagouv/infomedicament) : Enrichissement des données disponibles et amélioration de la recherche et de la navigation.
*   [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus) : Sécurisation des communications et amélioration de la testabilité.
*   [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back) : Amélioration de la gestion des données canoniques et optimisation de la chaîne CI/CD.
*   [test-sme](/repos/betagouv/test-sme) : Améliorations de l'interface utilisateur et de la gestion des pages.
