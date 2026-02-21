## Changelog : france-chaleur-urbaine-publicodes (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées au modèle Publicodes pour le comparateur France Chaleur Urbaine. Les mises à jour incluent des corrections de bugs, des ajustements des données (notamment concernant les aides financières et les dimensions de PAC), et des améliorations de l'infrastructure de publication. Une nouvelle version (1.4.0) a été publiée.

### Évolutions fonctionnelles
- Correction d'un bug sur les clés des tableaux et des graphiques (#f272b48).
- Mise à jour des données concernant les aides pour les solutions collectives à 35% (#4dd7761).
- Mise à jour des données pour le dimensionnement des PAC (#586518a, #f3d9366).
- Mise à jour des données pour le gaz individuel (P1) (#66a2285).
- Mise à jour des données pour la situation tertiaire moyenne (#0d0c4d0).
- Ajout de l'investissement P4 pour les sous-stations (#71b8d44).
- Correction de l'année d'enquête FEDENE pour 2024 (#06d7134).

### Évolutions techniques
- Passage à l'édition via "trusted publisher" pour la publication sur npmjs, supprimant ainsi le besoin du token NODE_AUTH_TOKEN (#99246fb, #3b6a630).
- Ajout d'un script pour obtenir les tableaux intermédiaires (#f9fa48a).
- Complétion du script `external-keys` avec les paramètres du simulateur (#350bffb).
- Ajout d'un test pour les clés utilisées par le comparateur (#986e642).
- Publication des versions 1.2.0, 1.3.0 et 1.4.0 (#c5836bc, #85e617e, #4c1060b).

### Autres changements
- Merge de la branche `dev` (#7be9cb6).
