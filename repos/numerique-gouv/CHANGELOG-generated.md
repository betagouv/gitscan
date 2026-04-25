# Synthèse d'activité : numerique-gouv (du 15/04 au 22/04)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de la sécurité, l'internationalisation et l'expérience utilisateur de ses différents services. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et améliorer les performances. [sites-faciles](/repos/numerique-gouv/sites-faciles) a notamment ajouté la gestion de plusieurs langues, tandis que [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) a renforcé la sécurité et amélioré la gestion des rôles. [b3desk](/repos/numerique-gouv/b3desk) a introduit la délégation de réunions et corrigé des bugs liés à l'interface utilisateur.

## Sécurité
Plusieurs changements liés à la sécurité ont été apportés :
- Correction d'une vulnérabilité potentielle concernant l'URL du secteur dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Restriction des types de fichiers autorisés dans [francetransfert](/repos/numerique-gouv/francetransfert) pour bloquer les fichiers HTML et HTM.

## Autres changements notables
- Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- Regroupement des points d'entrée de l'API dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) sous `/api/v1`.
- Correction d'un problème de configuration de l'environnement dans [statistiques-impact](/repos/numerique-gouv/statistiques-impact).

## Dépôts les plus actifs
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Mises à jour du système de design DSFR et corrections de bugs.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout de la gestion multilingue et amélioration des performances.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Amélioration de la sécurité, gestion des rôles et ajout de la gestion des zones géographiques.
- [b3desk](/repos/numerique-gouv/b3desk) : Implémentation de la délégation de réunions et corrections de bugs.
