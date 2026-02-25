## Changelog : france-chaleur-urbaine-publicodes (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives concernant les données utilisées pour les calculs, notamment pour les aides financières et le dimensionnement des pompes à chaleur. Des corrections de bugs ont également été apportées pour assurer la fiabilité des résultats et des tests unitaires ont été ajoutés pour garantir la qualité du code. Une nouvelle version (1.4.0) a été publiée, intégrant ces améliorations.

### Évolutions fonctionnelles
- Correction d'un bug concernant les clés des tableaux et des graphiques (#f272b48)
- Ajout du bilan sur 1 an pour les PAC hybrides, le solaire thermique et le système solaire combiné (reverté par la suite : #8b8bce9, #409a1bf)
- Mise à jour des données concernant les aides pour les solutions collectives à 35% (#4dd7761)
- Mise à jour des données P1 gaz individuel et situation tertiaire moyen (#66a2285, #0d0c4d0)
- Mise à jour du dimensionnement des PAC (#586518a, #f3d9366)
- Ajout d'un investissement P4 pour les sous-stations (#71b8d44)

### Évolutions techniques
- Passage à la publication "trusted publisher" sur npmjs, supprimant la nécessité d'un token d'authentification dans le CI/CD (#99246fb, #3b6a630)
- Ajout d'un script pour obtenir les tableaux intermédiaires et compléter le script external-keys (#350bffb, #f9fa48a)
- Ajout de tests unitaires pour vérifier les clés utilisées par le comparateur (#986e642)
- Correction de l'année d'enquête FEDENE pour 2024 (#06d7134)
- Publication des versions 1.2.0, 1.3.0 et 1.4.0 (#c5836bc, #85e617e, #4c1060b)
