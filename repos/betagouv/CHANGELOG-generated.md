# Synthèse d'activité : betagouv (du 01/05 au 31/05)

## Résumé de l'activité
L'organisation betagouv a connu une période d'activité soutenue, marquée par des améliorations significatives en termes de sécurité, de performance et d'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour importantes, notamment *mon-entreprise*, *reva*, *sante-psy* et *infomedicament*, avec des fonctionnalités nouvelles ou améliorées pour les utilisateurs. L'accent a également été mis sur la maintenance technique, avec des mises à jour de dépendances et des refactorisations de code pour assurer la stabilité et la pérennité des projets. De nombreux projets ont également bénéficié d'améliorations de l'interface utilisateur, notamment l'adoption du Design System de l'État (DSFR) dans *eva-serveur*.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction d'une vulnérabilité critique dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) avec la mise à jour de la gem `rack-session`.
*   Correction d'une faille de sécurité dans [eva-serveur](/repos/betagouv/eva-serveur) concernant une injection SQL et une vulnérabilité sur TarteauCitronJS.
*   Mise à jour de dépendances dans plusieurs projets pour corriger des vulnérabilités potentielles (ex: *matomo-to-pg*, *infomedicament-html-parser*).
*   Renforcement de la sécurité de l'authentification avec l'ajout d'une vérification du certificat MQC dans [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng).

## Autres changements notables
*   **Refonte majeure de l'interface utilisateur :** Adoption du Design System de l'État (DSFR) dans [eva-serveur](/repos/betagouv/eva-serveur) pour une meilleure cohérence et accessibilité.
*   **Migration vers Next.js :** Mise à jour vers Next.js 16 dans [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) pour des performances améliorées et une meilleure expérience développeur.
*   **Refactorisation importante :** Refactorisation du code dans [nitrates](/repos/betagouv/nitrates) et [infomedicament](/repos/betagouv/infomedicament) pour améliorer la maintenabilité et la performance.
*   **Amélioration de l'importation de données :** Amélioration de l'importation depuis Airtable dans [grist-core](/repos/betagouv/grist-core).
*   **Modernisation de l'infrastructure :** Passage à Poetry pour la gestion des dépendances dans [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng).

## Dépôts les plus actifs
*   [zacharie](/repos/betagouv/zacharie) : Ajout de nouvelles fonctionnalités et améliorations de l'interface utilisateur pour la gestion des carcasses.
*   [test-sme](/repos/betagouv/test-sme) : Améliorations de l'expérience utilisateur, corrections de bugs et mises à jour techniques.
*   [sylvasan](/repos/betagouv/sylvasan) : Ajout de nouvelles fonctionnalités pour la création de formulaires et l'authentification.
*   [signalement-entreprise](/repos/betagouv/signalement-entreprise) : Correction de bugs et amélioration de la stabilité de l'API.
*   [mon-entreprise](/repos/betagouv/mon-entreprise) : Mise à jour de l'interface utilisateur et correction de bugs.
*   [reva](/repos/betagouv/reva) : Ajout de nouvelles fonctionnalités et améliorations de l'interface utilisateur pour la gestion des programmes.
*   [eva-serveur](/repos/betagouv/eva-serveur) : Adoption du DSFR et améliorations de la sécurité.
*   [infomedicament](/repos/betagouv/infomedicament) : Améliorations de la recherche sémantique et de la performance.
*   [euphrosyne](/repos/betagouv/euphrosyne) : Ajout de nouvelles fonctionnalités et corrections de bugs pour la gestion des participations.
*   [grist-core](/repos/betagouv/grist-core) : Amélioration de l'importation de données et de l'interface utilisateur.
