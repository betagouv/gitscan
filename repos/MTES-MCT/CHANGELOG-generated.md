# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité

L'organisation MTES-MCT a connu une semaine riche en activités, avec des améliorations significatives apportées à plusieurs de ses dépôts. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment via des refontes d'interfaces (Dossier-Facile-Frontend, acceslibre, ecobalyse), l'ajout de nouvelles fonctionnalités (Docurba, potentiel, vizeau), et l'amélioration de la qualité et de la sécurité des données (ecobalyse-data, td-mass-validator, sparte).  Plusieurs dépôts ont également bénéficié de mises à jour techniques importantes, comme la migration vers des versions plus récentes de frameworks (ecobalyse-method-tooling, stop-punaises) et l'optimisation des performances (monitorenv, vizeau). L'accent a été mis sur la correction de bugs et l'amélioration de la robustesse des applications.

## Sécurité

Plusieurs dépôts ont bénéficié de mises à jour de sécurité :

- Mise à jour de la dépendance `sentry-sdk` dans [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) pour corriger des vulnérabilités.
- Mise à jour des dépendances npm et yarn dans [vizeau](/repos/MTES-MCT/vizeau) pour corriger des vulnérabilités (CVE-2026-21440 et CVE-2026-22814).

## Autres changements notables

- **Modernisation technologique :** Migration vers Symfony 7.4 dans [stop-punaises](/repos/MTES-MCT/stop-punaises) pour une meilleure stabilité et sécurité.
- **Gestion des données :** Amélioration de la gestion des données et de la conformité dans plusieurs dépôts, notamment [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data) et [trackdechets-data](/repos/MTES-MCT/trackdechets-data).
- **Amélioration de l'API :** Ajout d'une authentification basique par token dans [aigle-api](/repos/MTES-MCT/aigle-api) pour sécuriser l'accès.
- **Refonte d'interfaces :** Refonte complète de la page de résultats dans [otelo-front](/repos/MTES-MCT/otelo-front) et amélioration significative de l'interface utilisateur dans [acceslibre](/repos/MTES-MCT/acceslibre).
- **Intégration DataGouv :** Amélioration de l'intégration avec DataGouv dans [sparte](/repos/MTES-MCT/sparte) pour la publication des données.

## Dépôts les plus actifs

- [Docurba](/repos/MTES-MCT/Docurba) : Ajout de nouvelles fonctionnalités pour la navigation par département et l'accès aux modules pour les utilisateurs DDT et PPA.
- [Dossier-Facile-Frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) : Refonte majeure de la gestion des liens de partage avec une nouvelle interface dédiée.
- [acceslibre](/repos/MTES-MCT/acceslibre) : Amélioration de l'interface utilisateur, de la gestion des contributions et de l'import de données.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Ajout de nouvelles fonctionnalités pour la gestion des déclarations et des documents.
- [vizeau](/repos/MTES-MCT/vizeau) : Ajout de nouvelles fonctionnalités pour la gestion des contrôles, l'édition des millésimes passés et l'attribution de parcelles.
