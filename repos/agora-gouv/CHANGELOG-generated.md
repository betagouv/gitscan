# Synthèse d'activité : agora-gouv (du 28 juin au 28 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'amélioration de la plateforme, tant en termes de stabilité et de sécurité que de fonctionnalités. Des efforts importants ont été déployés pour optimiser la gestion des certificats (ACME, Sectigo) et des liens profonds, améliorant ainsi l'expérience utilisateur sur mobile.  Des améliorations ont également été apportées à l'interface utilisateur, notamment via l'alignement sur le Design System FR, et à la gestion du contenu via le CMS Strapi. Les dépôts [agora-front](/repos/agora-gouv/agora-front), [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) et [agora-back](/repos/agora-gouv/agora-back) ont été particulièrement actifs.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité de la plateforme :
- Implémentation de l'automatisation Sectigo via ACME pour la gestion des certificats ([agora-back](/repos/agora-gouv/agora-back)).
- Ajout de certificats Sectigo pour améliorer la sécurité de l'application mobile ([agora-app](/repos/agora-gouv/agora-app)).
- Correction des empreintes de certificats SHA256 ([agora-front](/repos/agora-gouv/agora-front)).
- Ajout de SHA256 pour le débogage des liens profonds ([agora-front](/repos/agora-gouv/agora-front)).

## Autres changements notables
- Migration de la plateforme [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) vers Strapi V5.
- Refonte de l'algorithme de calcul des tendances (V3 et V4) sur [agora-back](/repos/agora-gouv/agora-back).
- Simplification du flush du cache Redis sur [agora-back](/repos/agora-gouv/agora-back).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Amélioration de la gestion des consultations, de la sélection des questions et ajout de fonctionnalités d'administration.
- [agora-front](/repos/agora-gouv/agora-front) : Corrections de bugs, améliorations de la sécurité et du design de l'interface utilisateur.
- [agora-app](/repos/agora-gouv/agora-app) : Amélioration de l'expérience utilisateur mobile avec corrections de liens profonds et de partage de contenu.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers Strapi V5 et ajout de nouvelles fonctionnalités pour la gestion du contenu.
