# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des avancées significatives sur plusieurs fronts chez etalab. L'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a été enrichie de nouvelles API et améliorée en termes de sécurité et de performance. Le domaine du transport a été particulièrement actif, avec des mises à jour des données de covoiturage ([lieux-covoiturage](/repos/etalab/lieux-covoiturage), [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage)), une évolution du profil NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)) et des améliorations majeures du site de publication des normes de transport ([transport-site](/repos/etalab/transport-site)).  L'outil Data Pass ([data_pass](/repos/etalab/data_pass)) a également progressé avec l'intégration de nouvelles API et une interface d'administration améliorée.

## Sécurité
- Migration des scopes des tokens vers les demandes d'autorisation et rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.

## Autres changements notables
- Mise à jour de Postgres et TimescaleDB dans l'environnement CI de [transport-site](/repos/etalab/transport-site).
- Publication de la v2.4.0 du profil France NeTEx dans [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) avec des modifications structurelles importantes.
- Amélioration significative de la recherche et de la validation NeTEx sur [transport-site](/repos/etalab/transport-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles API et amélioration de la sécurité et de la performance de l'API d'administration.
- [data_pass](/repos/etalab/data_pass) : Intégration de nouvelles API et ajout d'une interface d'administration pour les habilitations.
- [transport-site](/repos/etalab/transport-site) : Améliorations majeures de la recherche, de la validation NeTEx et de l'affichage des métadonnées.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 du profil France NeTEx avec des clarifications et des améliorations.
- [lieux-covoiturage](/repos/etalab/lieux-covoiturage) et [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données de covoiturage avec de nouveaux lieux.
