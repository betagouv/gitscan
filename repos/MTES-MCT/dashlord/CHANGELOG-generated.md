## Changelog : dashlord (30 derniers jours, au 24 mai 2026)

### Résumé
Ce mois-ci, les mises à jour de Dashlord se sont concentrées sur la synchronisation des URLs des différents services surveillés.  Un effort a été fait pour mettre à jour les adresses des sites hébergés sur beta.gouv.fr, ainsi que pour ajuster la configuration des outils de surveillance et des rapports.

### Évolutions fonctionnelles
- Mise à jour des URLs de plusieurs services surveillés, incluant notamment : prelex, pitchou, mesads, boris, vigieau, zlv, dialog, zerologementvacant, emile, ecobalyse, transport.data.gouv.fr, api.trackdechets, trackdechets, oilhi, mondiagartif, api.resorption-bidonvilles, prelevements-deau, resorption-bidonvilles, potentiel, mission-transition, partaj, mon-devis-sans-oublis, mobilic, le.taxi, stop-punaises, signal-logement, haie, envergo, france-chaleur-urbaine, filigrane, bo.dossierfacile.fr, api.dossierfacile.logement.gouv.fr, proprietaire.dossierfacile.fr, locataire.dossierfacile.logement.gouv.fr, docurba, doc.covoiturage.beta.gouv.fr, tech.covoiturage.beta.gouv.fr, attestation.covoiturage.beta.gouv.fr, covoiturage.beta.gouv.fr, app.covoiturage.beta.gouv.fr, carbone, camino, api.camino.beta.gouv.fr, aquapreneur, acceslibre, aides-territoires, apilos.logement.gouv.fr [#45](https://github.com/MTES-MCT/dashlord/pull/45).
- Ajout de Prelex aux services surveillés et basculement de l'URL d'Emile vers l'application (emile.beta.gouv.fr).

### Évolutions techniques
- Mise à jour de l'URL de l'API dans le fichier `dashlord.yml` [#45](https://github.com/MTES-MCT/dashlord/pull/45).
- Suppression de l'entrée a-dock du fichier `dashlord.yml`.
- Ajustement de la configuration des outils de surveillance (désactivation des statistiques, du budget, de Dependabot et Codescan) et désactivation de BetaGouv pour Prelex.

### Autres changements
- Mise à jour régulière du rapport de Dashlord.
