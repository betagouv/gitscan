# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité
L'activité de l'organisation MTES-MCT au cours des 7 derniers jours a été particulièrement riche et diversifiée, touchant de nombreux projets. On observe une forte concentration sur l'amélioration de la qualité des données et de l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour significatives, notamment [apilos](/repos/MTES-MCT/apilos) avec l'export des conventions vers S3, [acceslibre](/repos/MTES-MCT/acceslibre) avec l'intégration de données Literalis et l'amélioration de l'affichage des ERP, et [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data) avec l'enrichissement des données et la correction de doublons. Des efforts importants ont également été consacrés à la sécurité, avec des mises à jour de dépendances dans plusieurs dépôts comme [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) et [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités de sécurité :
- [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) a mis à jour `sentry-sdk`.
- [trackdechets](/repos/MTES-MCT/trackdechets) a renforcé la sécurité des hash d'invitation et amélioré le rate limiting.
- [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) a corrigé des vulnérabilités via la mise à jour de dépendances.

## Autres changements notables
- [Docurba](/repos/MTES-MCT/Docurba) a subi une refonte de son architecture Django et une migration vers la version 6.0, améliorant ainsi sa performance et sa maintenabilité.
- [acceslibre-schema](/repos/MTES-MCT/acceslibre-schema) a introduit la gestion de schémas multiples pour différents types de bâtiments, passant au format datapackage.
- [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) a bénéficié de l'ajout de déploiements automatisés sur Scaleway et de l'intégration de Sentry pour la surveillance des erreurs.
- [qualicharge](/repos/MTES-MCT/qualicharge) a été mis à jour vers Symfony 7.4.

## Dépôts les plus actifs
- [Docurba](/repos/MTES-MCT/Docurba) : Refonte de l'architecture et amélioration des fonctionnalités d'administration.
- [acceslibre](/repos/MTES-MCT/acceslibre) : Intégration de nouvelles sources de données et amélioration de l'interface utilisateur.
- [apilos](/repos/MTES-MCT/apilos) : Optimisation des performances et ajout de nouvelles fonctionnalités d'export.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Amélioration de la sécurité et ajout de nouvelles fonctionnalités pour la gestion des données.
- [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant) : Amélioration de la gestion des campagnes et des droits d'accès.
