# Synthèse d'activité : gip-inclusion (du 20/06 au 20/08)

## Résumé de l'activité
L'activité de cette période est marquée par des transformations majeures de l'expérience utilisateur et de l'architecture des services. Plusieurs plateformes ont bénéficié de refontes visuelles et fonctionnelles importantes, comme [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) (rebranding en Match Europe), visant à simplifier les parcours et à enrichir les outils de matching. Parallèlement, l'accent a été mis sur l'intelligence de la recherche et la fiabilité des données avec des optimisations significatives dans [dora](/repos/gip-inclusion/dora) et [data-inclusion](/repos/gip-inclusion/data-inclusion).

L'organisation renforce également ses standards d'accessibilité et d'internationalisation, notamment via [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025) et [itou-theme](/repos/gip-inclusion/itou-theme), tout en modernisant ses infrastructures de déploiement pour gagner en scalabilité et en robustesse.

## Sécurité
- Renforcement de la protection des données personnelles via l'anonymisation automatique des numéros NIR dans [autometa](/repos/gip-inclusion/autometa) et la gestion sécurisée des sorties nominatives dans [sps-emailer](/repos/gip-inclusion/sps-emailer).
- Amélioration de la sécurité des accès avec la refonte du parcours de double authentification (2FA) dans [les-emplois](/repos/gip-inclusion/les-emplois) et la restriction des téléchargements aux utilisateurs authentifiés dans [le-marche](/repos/gip-inclusion/le-marche).
- Sécurisation des infrastructures par la suppression de mots de passe codés en dur dans [fluo-proto](/repos/gip-inclusion/fluo-proto), le renforcement des routes OTP dans [les-emplois](/repos/gip-inclusion/les-emplois) et la normalisation des mots de passe dans [dora](/repos/gip-inclusion/dora).
- Généralisation du protocole HTTPS pour sécuriser la génération des URL dans [la-communaute](/repos/gip-inclusion/la-communaute).

## Autres changements notables
- Migrations architecturales majeures, notamment le passage à Django pour [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) et l'évolution vers des conteneurs serverless pour [fluo-proto](/repos/gip-inclusion/fluo-proto).
- Refonte structurelle des données, particulièrement la migration massive du modèle "Publics" dans [dora](/repos/gip-inclusion/dora).
- Évolutions de l'orchestration et de l'analyse de données avec l'intégration de nouveaux flux (DORA, IMER) dans [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow).
- Mise en place de l'internationalisation (i18n) pour [site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025).

## Dépôts les plus actifs
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding complet vers Match Europe et mise en place d'un flux de candidatures spontanées.
- [dora](/repos/gip-inclusion/dora) : Refonte profonde de la structure des données et optimisation du moteur de recherche.
- [plateforme-accueil](/repos/gip-inclusion/plateforme-accueil) : Refonte de la page d'accueil et migration vers une architecture Django.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Intégration de nouveaux modules d'orientation et renforcement de la sécurité des accès.
- [immersion-facile](/repos/gip-inclusion/immersion-facile) : Amélioration des tableaux de bord et de la gestion des conventions.
